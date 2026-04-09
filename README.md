# Django Task

This project is ready to deploy on Render with:

- a Python web service
- a free Render Postgres database
- Gunicorn for serving Django
- WhiteNoise for static files

## Render deploy steps

1. Push this project to GitHub.
2. In Render, create a new Blueprint instance from the repository.
3. Render will read `render.yaml` and create the web service plus Postgres database.
4. Wait for the first deploy to finish.
5. Open the generated `.onrender.com` URL.

## Important note about uploaded images

This app stores uploaded images on the local filesystem. Render Free web services use an ephemeral filesystem, so uploaded media files are lost whenever the service redeploys, restarts, or spins down.

If you want uploads to persist, use one of these:

- switch to a paid Render web service and attach a persistent disk
- move media storage to a cloud service like Cloudinary or S3
