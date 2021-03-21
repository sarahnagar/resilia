# Bordas

<p class="description">Use os utilitários de borda para rapidamente estilizar "border" e "border-radius" de um elemento. Ótimo para imagens, botões ou qualquer outro elemento.</p>

## Border

Use border utilities to add or remove an element's borders. Escolha para todas as bordas ou separadamente.

### Adicionando

{{"demo": "pages/system/borders/BorderAdditive.js", "defaultCodeOpen": false, "bg": true}}

```jsx
<Box sx={{ border: 1 }}>…
<Box border={1}>…
<Box borderTop={1}>…
<Box borderRight={1}>…
<Box borderBottom={1}>…
<Box borderLeft={1}>…
<Box borderRight={1}>…
<Box borderBottom={1}>…
<Box borderLeft={1}>…
<Box border={1}>…
<Box sx={{ borderTop: 1 }}>…
<Box borderRight={1}>…
<Box borderBottom={1}>…
<Box borderLeft={1}>…
<Box sx={{ borderRight: 1 }}>…
<Box m={1}>…
<Box p={2}>…
<Box m={1}>…
<Box p={2}>…
<Box sx={{ borderBottom: 1 }}>…
<Box m={1}>…
<Box p={2}>…
<Box m={1}>…
<Box p={2}>…
<Box sx={{ border: 1 }}>…
<Box border={1}>…
<Box borderTop={1}>…
<Box borderRight={1}>…
<Box borderBottom={1}>…
<Box borderLeft={1}>…
<Box borderRight={1}>…
<Box borderBottom={1}>…
<Box borderLeft={1}>…
<Box border={1}>…
<Box sx={{ borderTop: 1 }}>…
<Box borderRight={1}>…
<Box borderBottom={1}>…
<Box borderLeft={1}>…
<Box sx={{ borderRight: 1 }}>…
<Box m={1}>…
<Box p={2}>…
<Box m={1}>…
<Box p={2}>…
<Box sx={{ borderBottom: 1 }}>…
<Box m={1}>…
<Box p={2}>…
<Box m={1}>…
<Box p={2}>…
<Box sx={{ borderLeft: 1 }}>…
<Box m={1}>…
<Box p={2}>…
<Box m={1}>…
<Box p={2}>…
```

### Removendo

{{"demo": "pages/system/borders/BorderSubtractive.js", "defaultCodeOpen": false, "bg": true}}

```jsx
<Box sx={{ border: 0 }}>…
<Box border={0}>…
<Box borderTop={0}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box border={0}>…
<Box sx={{ borderTop: 0 }}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box border={0}>…
<Box sx={{ borderRight: 0 }}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box sx={{ border: 0 }}>…
<Box border={0}>…
<Box borderTop={0}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box border={0}>…
<Box sx={{ borderTop: 0 }}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box border={0}>…
<Box sx={{ borderRight: 0 }}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box border={0}>…
<Box sx={{ borderBottom: 0 }}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box border={0}>…
<Box sx={{ borderLeft: 0 }}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
<Box border={0}>…
<Box sx={{ borderLeft: 0 }}>…
<Box borderRight={0}>…
<Box borderBottom={0}>…
<Box borderLeft={0}>…
```

## Cor da Borda

{{"demo": "pages/system/borders/BorderColor.js", "defaultCodeOpen": false}}

```jsx
<Box sx={{ borderColor: 'primary.main' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box sx={{ borderColor: 'secondary.main' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box sx={{ borderColor: 'error.main' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box sx={{ borderColor: 'grey.500' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box sx={{ borderColor: 'primary.main' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box sx={{ borderColor: 'secondary.main' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box sx={{ borderColor: 'error.main' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box sx={{ borderColor: 'grey.500' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
<Box borderColor="primary.main">…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box sx={{ borderColor: 'text.primary' }}>…
<Box borderColor="secondary.main">…
<Box borderColor="error.main">…
<Box borderColor="grey.500">…
<Box borderColor="text.primary">…
```

## Border-radius

{{"demo": "pages/system/borders/BorderRadius.js", "defaultCodeOpen": false}}

```jsx
<Box sx={{ borderRadius: '50%' }}>…
<Box borderRadius="borderRadius">…
<Box borderRadius={16}>…
<Box borderRadius="borderRadius">…
<Box borderRadius={16}>…
<Box sx={{ borderRadius: 1 }}>…
<Box borderRadius="borderRadius">…
<Box borderRadius={16}>…
<Box borderRadius="borderRadius">…
<Box borderRadius={16}>… // theme.shape.borderRadius * 1
<Box sx={{ borderRadius: 16 }}>…
```

## API

```js
import { borders } from '@material-ui/system';
```

| Nome da importação | Propriedade    | Propriedade CSS | Chave do tema                                                    |
|:------------------ |:-------------- |:--------------- |:---------------------------------------------------------------- |
| `border`           | `border`       | `border`        | `borders`                                                        |
| `borderTop`        | `borderTop`    | `border-top`    | `borders`                                                        |
| `borderLeft`       | `borderLeft`   | `border-left`   | `borders`                                                        |
| `borderRight`      | `borderRight`  | `border-right`  | `borders`                                                        |
| `borderBottom`     | `borderBottom` | `border-bottom` | `borders`                                                        |
| `borderColor`      | `borderColor`  | `border-color`  | [`palette`](/customization/default-theme/?expand-path=$.palette) |
| `borderRadius`     | `borderRadius` | `border-radius` | [`shape`](/customization/default-theme/?expand-path=$.shape)     |