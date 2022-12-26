# clover-web-integration

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

The repo provides a simple way to generate an authentication token for testing [Clover](https://docs.clover.com/docs/using-api-tokens) APIs.

## Prerequisite

1. Create Clover developer account
2. Create Clover Web Application, ensure proper authentication flags are turned on for the required APIs
3. Python >= 3.8
4. [PDM](https://pdm.fming.dev/latest/)
5. Set environment variable `CLOVER_SECRET` with you application secret

## Running

To execute the authentication web-service use:

`pdm run start`

If you're running locally it is use [ngrok](https://ngrok.com/) or similar tool, to configure the route for the Clover App authentication.

Use the Clover POS to initiate a call for the web-app, and see the printed results. To use Clover APIs you will need the merchant-id and the printed authentication token

Good luck!
