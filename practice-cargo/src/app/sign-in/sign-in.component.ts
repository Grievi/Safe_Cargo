import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { RouterModule, Routes } from '@angular/router';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';


@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css'],
})
export class SignInComponent implements OnInit {
  constructor(private Router: ActivatedRoute) {}

  ngOnInit(): void {}
}
