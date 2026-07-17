# Diseño: Sección BENEFICIOS en /home

**Fecha:** 2026-07-17
**Alcance:** `medidor/app/templates/app/home.html` — sección `<section class="hm-benefits">` (líneas ~966-989)

## Contexto

La sección BENEFICIOS actual muestra solo 3 tarjetas genéricas (Fácil de implementar,
Reducción de pérdidas, Costo accesible). El usuario proporcionó la lista completa de
características técnicas del medidor y pidió reorganizar/ampliar los beneficios con datos
reales del producto, sin saturar la sección con demasiadas tarjetas.

Esta es la primera de varias mejoras planeadas para `/home` (el usuario indicó que hay más
contenido por analizar más adelante); esta iteración se limita a la sección BENEFICIOS.

## Decisiones de diseño

- **Cantidad de tarjetas:** 9 (no 12). Las 3 tarjetas originales (Fácil de implementar,
  Reducción de pérdidas, Costo accesible) se fusionan como contenido dentro de 2 de las 9
  tarjetas nuevas, en vez de mantenerse como tarjetas aparte.
- **Layout:** grid ampliado de 3 columnas, reutilizando la estructura y clases CSS actuales
  (`hm-benefits-grid`, `hm-benefit-card`, `hm-benefit-icon`). El grid ya es responsivo
  (3 col desktop → 2 col ≤1100px → 1 col ≤820px vía `base.css`/inline styles existentes en
  `home.html`), por lo que 9 tarjetas heredan ese comportamiento sin cambios adicionales.
- **Íconos:** estilo emoji/carácter dentro del círculo de color, igual que el patrón actual
  (`✓`, `💧`, `$`). No se requieren assets nuevos.
- **Interactividad:** se mantiene el hover actual de la tarjeta (`translateY` + sombra vía
  `.hm-benefit-card:hover`). No se agrega JS ni animaciones nuevas en esta iteración.

## Contenido final — 9 tarjetas

1. **🔄 Doble sistema de medición**
   Cuenta con medición análoga y digital: si uno de los sistemas falla, el otro continúa
   registrando, garantizando continuidad en el servicio.

2. **💧 Detecta fraudes, fugas y pérdidas**
   *(incluye la antigua tarjeta "Reducción de pérdidas")*
   Con tecnología anti-manipulación detecta flujo inverso e intervenciones de terceros. Con
   monitoreo avanzado identifica y previene fugas de agua, asegurando un uso eficiente del
   recurso y minimizando el desperdicio.

3. **📡 Lecturas remotas hasta 1 km**
   Tecnología de radiofrecuencia sin necesidad de internet: permite tomar lecturas sin
   ingresar a la propiedad, reduciendo costo y tiempo.

4. **🚰 Corte y reposición a distancia**
   Corta y repone el servicio de forma remota, sin necesidad de visitas a terreno.

5. **🧾 Facturación más precisa**
   Mayor precisión en las lecturas: disminuye errores de lectura manual y mejora la
   exactitud de la facturación.

6. **🛠️ Fácil de implementar y a un costo accesible**
   *(incluye las antiguas tarjetas "Fácil de implementar" y "Costo accesible")*
   Diseñado para simplificar el proceso de instalación —similar a un medidor tradicional,
   compatible con cañerías de 1/2" y 3/4"—, se adapta a cualquier comunidad reduciendo
   tiempos y costos operativos. Con batería de hasta 30 años de duración, garantía de 1 año
   en el medidor y garantía indefinida en el capturador, ofrecemos tecnología de calidad al
   alcance de cualquier comunidad.

7. **🛡️ Mayor seguridad para tus trabajadores**
   Al no requerir acceso frecuente a los domicilios, disminuye el riesgo para el personal
   técnico.

8. **📜 Certificado y con soporte real**
   Certificado por Dictuc y validado para uso en sistemas APR, con capacitación para tu
   equipo y soporte técnico sin costo.

9. **🏆 Respaldado por la experiencia**
   Más de 50.000 medidores entregados y casi 200 comunidades APR ya confían en nuestra
   tecnología, desarrollada en Chile.

## Fuera de alcance (explícitamente no incluido aquí)

- La sección "¿Qué hace nuestro medidor?" (`hm-features-section`, grid de 5 íconos) no se
  modifica en esta iteración.
- La sección "Sostenible" (`hm-sos-wrap`) no se modifica.
- No se agregan nuevas tarjetas más allá de las 9 definidas.
- No se agrega interactividad más allá del hover ya existente.

## Implementación (resumen para el plan)

- Reemplazar el `<h2>` y el contenido interno de `.hm-benefits-grid` en `home.html` con las
  9 tarjetas `.hm-benefit-card` listadas arriba (mismo markup/clases que las 3 actuales).
- No se requieren cambios de CSS: `.hm-benefits-grid`, `.hm-benefit-card`,
  `.hm-benefit-icon` y sus breakpoints responsivos ya soportan más ítems.
- No se requieren cambios en `views.py` ni assets estáticos nuevos.
