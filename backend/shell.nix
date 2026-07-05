{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "fastapi-flutter-backend-env";

  # Native system packages needed during development
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.virtualenv
    
    # Common native dependencies often required by Python C-extensions (like cryptography/pydantic)
    openssl
    stdenv.cc.cc.lib
  ];

  # Environment variables configuration
  shellHook = ''
    # Set up a local virtual environment if it doesn't exist
    if [ ! -d ".venv" ]; then
      echo "Creating virtual environment..."
      virtualenv .venv
    fi

    # Activate the virtual environment automatically
    source .venv/bin/activate

    # Ensure pip, setuptools, and wheel are up to date
    pip install --upgrade pip setuptools wheel > /dev/null

    # Install the core libraries needed for FastAPI + AI Streaming
    echo "Installing FastAPI, Uvicorn, and OpenAI SDK..."
    pip install fastapi uvicorn openai
    pip install python-dotenv
    # Fixes potential dynamic linker issues with certain binary Python wheels on NixOS
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH"

    echo ""
    echo "🚀 FastAPI Environment Ready!"
    echo "Run 'uvicorn main:app --reload' to start your backend."
    echo ""
  '';
}