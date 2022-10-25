var usuariocreado;
var num = 1;

for ( i = 0; i < num; i++) {

    var Login_Or_Regist = prompt("Bienvenido a JS!\nTiene cuenta en esta app?");

    if (Login_Or_Regist == "si") {

        var validar_nombre = prompt("Ingrese su nombre de usuario para validar");
        var validar_passwd = prompt("Ingrese su contraseña");

        if (contraseña_creado == validar_passwd || usuariocreado == validar_nombre) {
            alert("Bienvenido "+usuariocreado+"!");
        } else{
            alert("ERROR\nFavor ingrese bien la contraseña u usuario");
            num++;
        }

    } else if (Login_Or_Regist == "no") {
        var h = 1;
        for (let j = 0; j < h; j++) {

            var nombre_usuario_reg = prompt("Ingrese un nombre de usuario para el registro");
            var passwd = prompt("Ingrese una contraseña");
            var confirmacion = prompt("Quiere tener '" + nombre_usuario_reg + "' como nombre de usuario?");

            if (confirmacion == "si") {

                var conf_usuario = prompt("Ingrese nuevamente su nombre de usuario ");
                var conf_passwd = prompt("Ingrese su contraseña de usuario");

                if (conf_usuario == nombre_usuario_reg || conf_passwd == passwd) {
                                        
                    usuariocreado = conf_usuario;
                    contraseña_creado = conf_passwd;
                    alert("Se ha registrado con exito! "+ usuariocreado);
                    break;                    

                } else {
                    alert("Favor ingrese bien la contraseña o usuario")
                    h++;
                }

            } else if (confirmacion == "no") {
                h++;
            } else {
                alert("Favor oprimir ('si' o 'no')");
                h++;
            }

        }
    } else{
        alert("Solamente ingrese (si/no)");
        num++;
    }
}