import react from 'react';
import {BrowserRouter,Route,Link} from 'react-router-dom';
import {useState,useEffect} from 'react';

export default function Login(){
  const [username,setUsername]=useState("");
  const [password,setPassword]=useState("");
  const function handelSubmit(){
     
  }
  return (
    <div>
      <form onSubmit={}>
         <label>Username:</label>
         <input type="text" name="username" value={username} onChange={(event)=>{setUsername(event.target.value)}}/>
        <br/>
         <label>Password:</label> 
         <input type="password" name="password" value={password} onChange={(event)=>{setPassword(event.target.value)}}/>
          <input type="button" value="Submit"/>  
      </form> 
    </div>
  );
}
