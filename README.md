# Borrador de la futura Constitución de Chile

*Todos los artículos aprobados de la #NuevaConstitución de Chile a 1 solo click*

Este repositorio alberga el código para construir el sitio [leelanuevaconstitucion.cl](https://leelanuevaconstitucion.cl/), a partir de la transcripción de los artículos aprobados en particular por el pleno de la [Convención Constitucional](https://www.chileconvencion.cl/).

Está desarrollado usando el framework [Hugo](https://gohugo.io/) y toma como base el tema [Hugo Book](https://github.com/alex-shpak/hugo-book), desarrollado por [Alex Shpak](https://github.com/alex-shpak).

## Contenidos
La información a partir de la que se compila el sitio está contenida, casi en su totalidad, dentro de la carpeta `contents/comisiones`. Cada comisión está enumerada y cuénta con su propio índice (`_index.md`) para generar la vista conjunta de todos los artículos aprobados hasta el momento. 

## ¿Por qué Hugo?
- Es *rapidísimo*, no requiere instalar dependencias y el *built-in server* funciona de maravilla al momento de desarrollar,
- Se integra de manera muy sencilla con Github Actions!
- Como el sitio es principalmente para desplegar información que no cambia frecuentemente (a.k.a. *estático*), es mejor ahorrarse el back-end (tiempo de desarrollo y $$$),
- Quería aprender a ocuparlo :)

## ¿Te interesa colaborar?
Por ahora puedes colaborar de dos maneras:
- Proponer cambios de estilo para *facilitar* la lectura en todos los dispositivos posible, incluyendo aquellos para personas con discapacidad visual. Sólo es necesario seguir los siguientes lineamientos:
  - Mientras menos opciones, mejor
  - Mientras más legible, mejor
  - Mientras más concisa la información, mejor
- Corregir typos

En cualquier caso, siéntete libre de hacer un PR y/o abrir un Issue :)
