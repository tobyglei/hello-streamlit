mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"21yunbox@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
enableWebsocketCompression = false\n\
port = 10000\n\
[browser]\n\
gatherUsageStats = false\n\
" > ~/.streamlit/config.toml