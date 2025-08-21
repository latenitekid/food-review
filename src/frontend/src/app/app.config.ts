import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideAuth0 } from '@auth0/auth0-angular';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideClientHydration } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideClientHydration(),
    provideAuth0({
      domain: 'dev-nlm.us.auth0.com',
      clientId: 'so3cPHg0Rmw2gdirodEdVQdqqlZlfc8s',
      authorizationParams: {
        redirect_uri: "http://localhost:4200/callback",
      }
    })
  ]
};
