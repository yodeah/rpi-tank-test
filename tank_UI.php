<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <table>
            <tr>
                <td></td>
                <td><form method="post" action=""><input type="hidden" name="irany" value="elore"/><button>elore</button></form></td>
                <td></td>
            </tr>
            <tr>
                <td><form method="post" action=""><input type="hidden" name="irany" value="balra"/><button>balra</button></form></td>
                <td></td>
                <td><form method="post" action=""><input type="hidden" name="irany" value="jobbra"/><button>jobbra</button></form></td>
            </tr>
            <tr>
                <td></td>
                <td><form method="post" action=""><input type="hidden" name="irany" value="hatra"/><button>hatra</button></form></td>
                <td></td>
            </tr>
        </table>
        <?php
        error_reporting (E_ALL);

switch ($_POST['irany']) {
            case "elore":
                var_dump("IRANY: elore");
                var_dump(shell_exec ("sudo python /home/pi/rpi-tank-test/tank_iranyitas.py " . $_POST['irany']));
            case "balra":
                var_dump("IRANY: balra");
                var_dump(shell_exec ("sudo python /home/pi/rpi-tank-test/tank_iranyitas.py " . $_POST['irany']));
            case "jobbra":
                var_dump("IRANY: jobbra");
                var_dump(shell_exec ("sudo python /home/pi/rpi-tank-test/tank_iranyitas.py " . $_POST['irany']));
            case "hatra":
                var_dump("IRANY: hatra");
                var_dump(shell_exec ("sudo python /home/pi/rpi-tank-test/tank_iranyitas.py " . $_POST['irany']));

            default:
                break;
        }
        ?>
    </body>
</html>
