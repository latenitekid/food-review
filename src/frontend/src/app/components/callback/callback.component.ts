import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-callback',
  standalone: true,
  template: '<div>Processing login...</div>'
})
export class CallbackComponent implements OnInit {
  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit() {
    this.apiService.handleCallback().subscribe({
      next: () => {
        this.router.navigate(['/']);
      },
      error: (error) => {
        console.error('Error saving login: ', error);
        this.router.navigate(['/']);
      }
    });
  }
}
