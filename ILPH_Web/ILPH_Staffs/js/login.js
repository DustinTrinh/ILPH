
/*
1. Get Username Password input 
2. Connect to Database and search for that Username
3. if exist, grab password and DECODE -- If DNE, display errors
4. Redirect based on Role
*/ 
//const bcrypt = require('bcrypt');
//const { Pool } = require('pg');
function databaseConnect(username, password){
    
    var query = {
        // give the query a unique name
        name: 'searrch-user',
        text: 'SELECT * FROM public.users WHERE username = $1',
        values: [username]
      }
    const pool = new Pool({
        user: 'postgres',
        host: 'localhost',
        database: 'postgres',
        password: '080599',
        port: 5432,
      });
  
      pool.query(query, (err, res) => {
        
        if(Object.keys(res.rows).length > 0){
            //have username
            const check = decrypt(res.rows[0].password_hash);
            if(password == check)
            {
                window.location.href = "./main_staffs.html";
            }
            else{
                document.getElementById("errorLogin").innerHTML = " Please recheck your username and password";
            }
        }
        else{
            document.getElementById("errorLogin").innerHTML = "Your username does not exist in our system.";
        }

        pool.end()
      });
}

function decrypt(password){
    bcrypt.compare(password, safeHash, function(err, res) {
        return res;
    });
}

function login(){
    var usernameInput = document.getElementById("username").value;
    var passwordInput = document.getElementById("password").value;

    databaseConnect(usernameInput, passwordInput);

}
