# BrainHint — Frontend

Application Angular avec **Reactive Forms** et **Angular Material**.

## Stack

- Angular 19 (standalone components)
- Angular Material (thème `azure-blue`)
- Reactive Forms (`FormBuilder`, validators)
- CSS

## Démarrage

```bash
cd frontend
npm install
npm start
```

L'application est disponible sur [http://localhost:4200](http://localhost:4200).

## Structure

```
src/app/
├── layout/app-shell/   # mat-toolbar + mat-sidenav-container
├── pages/home/         # Exemple de formulaire réactif Material
├── app.config.ts       # Providers (router, animations)
└── app.routes.ts       # Routes
```

## Commandes utiles

| Commande        | Description              |
|-----------------|--------------------------|
| `npm start`     | Serveur de dev           |
| `npm run build` | Build de production      |
| `npm test`      | Tests unitaires (Karma)  |

## Ajouter un composant

```bash
npx ng generate component pages/ma-page
```
