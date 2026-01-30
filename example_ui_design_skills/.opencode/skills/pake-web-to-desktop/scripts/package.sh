#!/bin/bash

# Pake Web-to-Desktop Packaging Script
# Usage: ./scripts/package.sh [build-dir] [port] [app-name]

set -e

# Configuration
BUILD_DIR="${1:-dist}"
PORT="${2:-3000}"
APP_NAME="${3:-MyApp}"
ICON="${4:-}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo_step() {
    echo -e "${GREEN}==>${NC} $1"
}

echo_warn() {
    echo -e "${YELLOW}WARNING:${NC} $1"
}

echo_error() {
    echo -e "${RED}ERROR:${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    echo_step "Checking prerequisites..."

    # Check Node.js
    if ! command -v node &> /dev/null; then
        echo_error "Node.js is not installed. Please install Node.js >= 22"
        exit 1
    fi

    # Check Pake CLI
    if ! command -v pake &> /dev/null; then
        echo_warn "Pake CLI not found. Installing..."
        npm install -g pake-cli
    fi

    echo_step "Prerequisites check passed"
}

# Build the project
build_project() {
    echo_step "Building project in $BUILD_DIR..."

    if [ ! -d "$BUILD_DIR" ]; then
        echo_error "Build directory '$BUILD_DIR' not found. Run your build command first."
        echo "  npm run build   # for React/Vue/Vite"
        echo "  pnpm build"
        exit 1
    fi

    if [ ! -f "$BUILD_DIR/index.html" ]; then
        echo_error "index.html not found in $BUILD_DIR"
        exit 1
    fi

    echo_step "Build complete"
}

# Kill existing server
kill_server() {
    if [ ! -z "$SERVER_PID" ] && kill -0 $SERVER_PID 2>/dev/null; then
        echo_step "Stopping existing server (PID: $SERVER_PID)"
        kill $SERVER_PID 2>/dev/null || true
        wait $SERVER_PID 2>/dev/null || true
    fi
}

# Start local server
start_server() {
    echo_step "Starting local server on port $PORT..."

    # Try npx serve first, then python http.server
    if command -v npx &> /dev/null; then
        npx serve "$BUILD_DIR" -l "$PORT" &
        SERVER_PID=$!
    elif command -v python3 &> /dev/null; then
        cd "$BUILD_DIR" && python3 -m http.server "$PORT" &
        SERVER_PID=$!
    elif command -v python &> /dev/null; then
        cd "$BUILD_DIR" && python -m SimpleHTTPServer "$PORT" &
        SERVER_PID=$!
    else
        echo_error "No suitable server found. Install npx or Python."
        exit 1
    fi

    # Wait for server to start
    sleep 2

    if ! kill -0 $SERVER_PID 2>/dev/null; then
        echo_error "Failed to start server"
        exit 1
    fi

    echo_step "Server started (PID: $SERVER_PID)"
}

# Package with Pake
package_app() {
    echo_step "Packaging $APP_NAME..."

    URL="http://localhost:$PORT"

    # Build pake command
    PAKE_CMD="pake $URL --name \"$APP_NAME\""

    if [ ! -z "$ICON" ]; then
        PAKE_CMD="$PAKE_CMD --icon \"$ICON\""
    fi

    echo_step "Running: $PAKE_CMD"

    # Run pake
    eval "$PAKE_CMD"

    echo_step "Packaging complete!"
}

# Cleanup
cleanup() {
    echo_step "Cleaning up..."
    if [ ! -z "$SERVER_PID" ] && kill -0 $SERVER_PID 2>/dev/null; then
        kill $SERVER_PID 2>/dev/null || true
    fi
    echo_step "Done"
}

# Set trap for cleanup
trap cleanup EXIT INT TERM

# Main execution
main() {
    echo "========================================="
    echo "  Pake Web-to-Desktop Packaging Script"
    echo "========================================="
    echo ""
    echo "  Build Dir: $BUILD_DIR"
    echo "  Port:      $PORT"
    echo "  App Name:  $APP_NAME"
    echo "  Icon:      ${ICON:-auto}"
    echo ""
    echo "========================================="
    echo ""

    check_prerequisites
    build_project
    kill_server
    start_server
    package_app
}

main "$@"
