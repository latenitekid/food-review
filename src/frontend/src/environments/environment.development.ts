export const environment = {
  production: false,
  apiBaseUrl: 'http://localhost:8000',
  authConfig: {
    domain: 'dev-nlm.us.auth0.com',
    clientId: 'so3cPHg0Rmw2gdirodEdVQdqqlZlfc8s',
    redirect_uri: 'http://localhost:4200/callback',
    audience: 'http://localhost:8000/',
    scope: 'email profile openid'
  }
};
