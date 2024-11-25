import os
from app import create_app

if __name__ == '__main__':
    app = create_app()

    # Run the application
    port = int(os.getenv("PORT", 5000))  # Default port is 5000
    app.run(host="0.0.0.0", port=port, debug=True)
