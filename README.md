# Django Task

This project is ready to deploy on Render with:

- a Python web service
- a free Render Postgres database
- Gunicorn for serving Django
- WhiteNoise for static files
- Cloudinary for persistent uploaded post images

## Render deploy steps

1. Push this project to GitHub.
2. In Render, create a new Blueprint instance from the repository.
3. Render will read `render.yaml` and create the web service plus Postgres database.
4. Add these Render environment variables from your Cloudinary dashboard:

- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

5. Wait for the first deploy to finish.
6. Open the generated `.onrender.com` URL.

## Important note about uploaded images

This app uses Cloudinary for uploaded post images, so posts created by friends online can keep their images after Render restarts or redeploys.

Existing local files inside `media/` are not uploaded automatically. If you want those old local images online too, upload them again through the deployed site or manually add them to Cloudinary.
