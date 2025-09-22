import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { authHttpInterceptorFn, provideAuth0 } from '@auth0/auth0-angular';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideClientHydration } from '@angular/platform-browser';
import { provideHttpClient, withInterceptors } from '@angular/common/http';

import { environment } from '../environments/environment';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideClientHydration(),
    provideHttpClient(withInterceptors([authHttpInterceptorFn])),
    provideAuth0({
      domain: environment.authConfig.domain,
      clientId: environment.authConfig.clientId,
      authorizationParams: {
        redirect_uri: environment.authConfig.redirect_uri,
        audience: environment.authConfig.audience,
        scope: environment.authConfig.scope,
        responseType: 'token id_token'
      },
      httpInterceptor: {
        allowedList: [
          {
            uri: environment.apiBaseUrl + '/*',
            tokenOptions: {
              authorizationParams: {
                redirect_uri: environment.authConfig.redirect_uri,
                scope: environment.authConfig.scope,
                audience: environment.authConfig.audience,
                responseType: 'token id_token'
              }
            }
          }
        ]
      }
    })
  ]
};
