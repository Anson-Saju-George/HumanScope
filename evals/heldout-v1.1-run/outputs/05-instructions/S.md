## Rotate your API key

Before you start, make sure you have Admin access to the project. Only Admins see the Generate button.

Schedule rotation during low traffic: the old key stops working as soon as you generate a new one, so your app can't authenticate until it's redeployed with the new key.

1. Open **Project settings → API**.
2. Click **Generate new key**. The old key stops working immediately.
3. Copy the new key and paste it into your app's environment variables.
4. Redeploy your app.
