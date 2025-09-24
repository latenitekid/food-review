import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { AuthService } from '@auth0/auth0-angular';
import { catchError } from 'rxjs/operators';

@Component({
  selector: 'app-navbar',
  standalone: true,
  templateUrl: './navbar.component.html',
  imports: [RouterLink, RouterLinkActive, CommonModule],
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  constructor(public auth: AuthService) {}

  ngOnInit() {}

  login() {
    this.auth
      .loginWithRedirect()
      .pipe(
        catchError((error) => {
          console.error('Login failed: ', error);
          return [];
        })
      )
      .subscribe();
  }

  logout() {
    this.auth.logout({
      logoutParams: {
        returnTo: window.location.origin
      }
    });
  }
}
