# This script guides you through setting up environment variables on Railway.
# Follow these steps:

1. Go to your project in Railway at https://railway.app
2. Click on "Variables"
3. Add the following variables:

- SECRET_KEY (generate a secure random string)
- MAIL_USERNAME (your email service)
- MAIL_PASSWORD (your email app password)
- MAIL_DEFAULT_SENDER (email sender)
- PORT (usually set automatically by Railway)

4. Railway will automatically provide DATABASE_URL if you add a PostgreSQL database to your project.

# Setting up PostgreSQL on Railway:
1. Add a PostgreSQL database service to your project
2. Check that your config.py can handle the DATABASE_URL format (which we've fixed)

# Deploy your application:
1. Push your code to GitHub
2. Link your GitHub repo to Railway 
3. Railway should automatically deploy your application with the updated files
