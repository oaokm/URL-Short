from app import createApp


app = createApp()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9800)