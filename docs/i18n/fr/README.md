<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | **🇫🇷 Français** | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Chasseur de modèles pour arena.ai : lance un lot de discussions en mode agent, empreinte chaque réponse, identifie le modèle qui a répondu et renomme la discussion à son nom — le matin, vous avez une discussion étiquetée propulsée par Claude Opus, GPT-5, Gemini ou celui que vous cherchiez.**

![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![UI](https://img.shields.io/badge/UI-terminal-6E56CF)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

```
   +------------------------------------------------------------------+
   |                                                                  |
   |  *  arena model hunter                                           |
   |     arena.ai automation - v1.0.0                                 |
   |                                                                  |
   |  o Arena account connected  .  you@example.com                   |
   |  ~ mode: single-threaded  .  English                             |
   |                                                                  |
   |  > Start                                                ready    |
   |    Settings                                   account & exit     |
   |    Exit                                                          |
   |                                                                  |
   | arrows select    Enter open    q quit                            |
   |                                                                  |
   +------------------------------------------------------------------+
```

## 🎯 Pourquoi cet outil existe

En mode agent, arena.ai décide seul quel modèle répond, et ce n'est pas toujours celui que vous voulez : parfois un modèle de premier rang (Claude Opus et ses pairs), parfois beaucoup plus faible. Cet outil transforme cette loterie en recherche : il ouvre un lot de discussions en mode agent, rejoue les trois échantillons d'empreinte dans chacune, demande au site d'empreintes quel modèle a répondu et inscrit le verdict dans le titre de la discussion (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Laissez-le tourner la nuit avec autant de discussions que vous voulez ; au matin, la liste est étiquetée : ouvrez celle dont le titre nomme le modèle qu'il vous faut et travaillez dedans. Là est l'idée : non pas automatiser pour automatiser, mais obtenir une discussion qui tourne vraiment sur le modèle souhaité.

## ✨ Ce qu'elle fait

- **Une seule connexion — la session reste.** Une vraie fenêtre Chromium (jamais headless) s'ouvre, vous vous connectez à arena.ai normalement ; l'application détecte la connexion, enregistre la session et ferme elle-même le navigateur.
- **N conversations à la fois.** Vous saisissez un nombre de 1 à 100 — exactement autant d'onglets `arena.ai/agent` et autant d'onglets `lm.ikale.io` s'ouvrent.
- **Copie à votre place.** Le prompt de chaque échantillon part vers l'agent, la réponse est attendue en entier puis collée dans le champ Reply — trois échantillons par conversation.
- **Nomme le modèle.** Clique sur Verify sur le site d'empreintes, lit le meilleur candidat et la confiance exactement comme le site les affiche, puis renomme la conversation Arena en `modèle confiance` (par exemple `gpt-6-luna 99.9%`).
- **Deux modes d'exécution.** Mono-thread (sûr, conversations l'une après l'autre) et multi-thread (toutes en parallèle, 1,5–2× plus rapide).
- **Interface en trois langues.** English, Русский, 中文 — changeable dans l'application, sans redémarrage.

## 🔄 Comment se déroule une exécution

1. **Connexion** — le navigateur s'ouvre, vous vous authentifiez, l'application le détecte et ferme la fenêtre.
2. **Démarrer → nombre de conversations** — par exemple `3` : trois onglets Arena et trois onglets d'empreintes.
3. **Échantillons 1 → 3** — chaque prompt part vers l'agent, chaque réponse revient sur le site.
4. **Verify** — le site classe les modèles candidats, l'application lit le gagnant et la confiance.
5. **Renommage** — la conversation Arena s'appelle désormais `modèle confiance`, et un résumé s'affiche dans la console.

## 📋 Prérequis

- Python **3.10+**
- Windows 10/11, macOS ou Linux
- Un compte arena.ai (e-mail et mot de passe, ou lien reçu par e-mail)
- ~400 Mo d'espace libre pour Chromium de Playwright

## 🚀 Installation

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows :** il suffit ensuite de double-cliquer sur `run.bat` (il active l'UTF-8 pour un affichage correct du cyrillique).
**macOS / Linux :** `./run.sh` ou `python main.py`.

## 🕹️ Utilisation

```bash
python main.py
```

| Option | Description |
|---|---|
| **Démarrer** | demande combien de discussions lancer (1–100, ou n'importe quel nombre avec les discussions illimitées) et démarre tout le pipeline |
| **Réglages** | mode d'exécution, langue de l'interface, suppression du compte arena.ai actif |
| **Quitter** | ferme l'application (le terminal retrouve son contenu précédent) |

Le menu s'adapte à l'état : tant qu'aucun compte n'est connecté, **Se connecter** s'affiche et le curseur se place dessus ; après une connexion réussie, l'élément disparaît.

## ⚙️ Réglages

| Option | Description |
|---|---|
| **Mode d'exécution** | `mono-thread` (par défaut) / `multi-thread` — le multi-thread est plus rapide mais envoie des requêtes parallèles |
| **Langue** | `English` / `Русский` / `中文` — appliquée immédiatement et mémorisée |
| **Discussions illimitées** ⚠️ | supprime la limite de 100 discussions : `Start` accepte n'importe quel nombre — dangereux, désactivé par défaut |
| **Supprimer le compte arena.ai actif** | efface le profil du navigateur et la session, donc déconnecte |

Les réglages sont stockés dans `~/.arena-model-hunter/config.json` :

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Les discussions illimitées sont désactivées par défaut et l'avertissement n'est pas décoratif.** Une fois activées, `Start` accepte n'importe quel nombre au lieu de 1–100 — `250`, `1000`. Chaque discussion, ce sont deux onglets : des chiffres élevés signifient une rafale de requêtes parallèles vers arena.ai, exactement ce que les limites de débit et les captchas sont là pour arrêter, avec un vrai risque de restriction du compte. N'activez l'option que si vous l'acceptez, et restez en mode mono-thread ; au-delà de 100, une seconde confirmation rappelle le nombre exact avant que quoi que ce soit ne s'ouvre.

## 🔐 Comment fonctionne la connexion

1. Une fenêtre Chromium **réelle** s'ouvre avec un profil persistant (`~/.arena-model-hunter/profile`) — Cloudflare refuse les navigateurs headless, l'application n'en utilise donc jamais.
2. Vous cliquez sur `Log In` → saisissez votre e-mail → `Continue with email`.
   - Compte existant → saisissez le mot de passe → `Log In`.
   - Nouvel e-mail → l'étape du nom peut être ignorée → un lien arrive par e-mail → collez-le dans la barre d'adresse (`Ctrl+L`, `Ctrl+V`, Entrée) → créez un mot de passe.
3. L'application interroge la page toutes les 1,5 s et détecte la connexion à trois signes : votre e-mail apparaît dans la barre latérale, le cookie `arena-auth-*` apparaît, le bouton `Log In` disparaît.
4. Elle enregistre `session.json` + `state.json` et **ferme le navigateur**.

Le site s'ouvre toujours en **thème sombre** (le navigateur est lancé avec `prefers-color-scheme: dark`, ce que arena.ai respecte).

## ⚡ Mode mono-thread et multi-thread

| Mode | Fonctionnement | Mesuré sur 3 conversations |
|---|---|---|
| **Mono-thread** (par défaut) | les paires d'onglets sont traitées l'une après l'autre, l'onglet actif passe devant | ≈7,5 min |
| **Multi-thread** | toutes les paires d'onglets tournent en même temps, le focus n'est pas déplacé | ≈4,5 min |

En multi-thread, Arena reçoit plusieurs requêtes simultanément : les limites et les captchas sont plus probables. Si cela arrive, revenez au mode mono-thread.

## 🗂️ Structure du projet

```
arena-model-hunter/
├── main.py             # menu, réglages, scénarios
├── ui.py               # interface terminal : cadre, alt-screen, lecture des touches, redimensionnement
├── arena_login.py      # navigateur, connexion, détection de session, configuration
├── flow.py             # pipeline Arena ↔ lm.ikale.io, Verify, renommage
├── i18n.py             # traductions de l'interface (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI : lint et vérification des traductions
├── LICENSE
└── docs/i18n/          # ce README en 30 langues
```

## 🌍 Variables d'environnement

| Variable | Par défaut | Rôle |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | dossier du profil et de la session |
| `ARENA_HELPER_HOME` | — | ancien nom de la variable, toujours accepté |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | remplissage optionnel du formulaire (jamais enregistré) |
| `ARENA_LOGIN_TIMEOUT` | `900` | secondes d'attente pour la connexion |
| `ARENA_URL` | `https://arena.ai/` | URL de départ |

## 🧰 Questions fréquentes

- **« Just a moment… » / contrôle Cloudflare** — il faut une fenêtre de navigateur visible ; ne lancez pas sur un serveur sans bureau.
- **« Le navigateur n'est pas installé »** — lancez `python -m playwright install chromium`.
- **Captcha ou requêtes silencieusement ignorées** — vous avez probablement atteint une limite : passez en mono-thread et ralentissez.
- **Je veux repartir de zéro** — Réglages → *Supprimer le compte arena.ai actif*, ou supprimez `~/.arena-model-hunter`.
- **Chasser toute la nuit** — Réglages → *Discussions illimitées*, tapez `300` dans Démarrer et confirmez ; gardez le mode mono-thread et regardez les discussions renommées au matin.

## ⚠️ Avertissement

Ce projet est destiné à des **expérimentations personnelles et à l'apprentissage**. Il automatise un site tiers ; l'automatisation peut enfreindre les conditions d'utilisation d'arena.ai et du site d'empreintes et entraîner des restrictions de compte. Utilisez-le à vos risques, ne générez pas de charge inutile, restez en mono-thread en cas de doute et ne publiez jamais vos identifiants — l'application n'enregistre pas le mot de passe sur le disque.

## 📄 Licence

[MIT](LICENSE) — logiciel libre : vous pouvez l'utiliser, l'étudier, le partager et le modifier. Si vous distribuez le programme ou une version modifiée, vous devez y joindre la mention de copyright et le texte de la licence MIT. Aucune garantie.

Copyright (C) 2026 contributeurs d'arena model hunter.

