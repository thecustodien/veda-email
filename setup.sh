mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor=\"#000000\"\n\
backgroundColor=\"#89023e\"\n\
secondaryBackgroundColor=\"#19647e\"\n\
textColor=\"#ffffff\"\n\
font=\"monospace\"\n\
" > ~/.streamlit/config.toml