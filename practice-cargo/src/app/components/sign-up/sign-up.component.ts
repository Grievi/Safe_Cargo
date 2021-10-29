import { Component, OnInit } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Router } from '@angular/router';
import { User } from 'src/app/class/user';
import { UserService } from 'src/app/profiles/user.service';


@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  newUser :User[]=[]
  constructor(
    private UserApiLink:UserService
    ) {}
callOurApi(){
  this.UserApiLink.getUserApi().subscribe((newUser:any)=>{
    this.newUser=newUser
    console.log('New user api works',this.newUser)
  })
}
  ngOnInit(){
    this.callOurApi()
  }

}
