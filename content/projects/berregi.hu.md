+++
title = "berregi"
description = """
Egy kapucsengő vezeték nélkülivé alakítása két darab Raspberry Pi Pico mikrovezérlő segítségével,
amelyek egy meglévő, vezeték nélküli hálózaton keresztül TCP-kapcsolatot létesítenek egymással.
"""
date = 2024-05-06

[extra]
date_start = 2024-05-06
image = "berregi.png"
top_project = true

[taxonomies]
projects = ["Software Development (Embedded)"]
skills = ["Asynchronous I/O", "Embassy", "Rust"]
+++

Otthonfelújítás során a falról egy szakaszon lekerült a kapucsengő vezetéke. Úgy döntöttem, hogy
nem kötöm vissza a nyomógombot, hanem megragadom a lehetőséget, hogy átültessem a gyakorlatba az
újonnan szerzett Rust programozási nyelvi tudásomat. Szerettem volna beágyazott rendszerekkel is
foglalkozni, így terveztem és telepítettem egy vezeték nélküli rendszert a vezetékes helyett.

A rendszer és hozzá a szoftver a mai napig használatban van.

{{ icon(type="github") }}
<https://github.com/immersum/berregi>

## Felelősségi kör

* A kapucsengő működésének helyreállítása
* Raspberry Pi Pico **mikrovezérlők** programozása
* A Rust és vele együtt az **aszinkron** nyelvi paradigma használatának gyakorlása
