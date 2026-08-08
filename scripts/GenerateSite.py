import html
import os

# tags: pvp, frames, ui, qol, class, sound
ADDONS = [
    dict(name="FrameSort", icon="FrameSort.png", cf=709847, gh="framesort",
         tags=["pvp", "frames"], flavors=["Retail", "Classic"],
         tagline="Sorts party, raid and arena frames and puts you at the top, middle or bottom.",
         features=[
             "Place your own frame at the top, middle or bottom",
             "Sort the remaining frames by group, role or alphabetically",
             "Works with Blizzard, Gladius, GladiusEx, sArena, ElvUI and Cell",
             "Keybindings to target frames by their visual position rather than party number",
             "Macro variables for @Healer, @EnemyHealer, @Frame and more",
             "Add spacing between frames",
             "Automatically promote healers to leader in solo shuffle",
         ]),
    dict(name="MiniArenaDebuffs", icon="MiniArenaDebuffs.svg", cf=1421998, gh="mini-arena-debuffs",
         tags=["pvp", "frames"], flavors=["Retail"],
         tagline="Shows debuffs on arena frames.",
         features=[
             "Option to show only your own debuffs",
             "Debuffs sorted by time remaining",
             "Change the position and size of the debuff icons",
             "Anchors to arena frame addons such as sArena and GladiusEx",
             "Test mode with fake arena frames for easy configuration",
         ]),
    dict(name="MiniAuras", icon="MiniAuras.svg", cf=1439482, gh="mini-auras",
         tags=["pvp", "frames"], flavors=["Retail"],
         tagline="Tracks CC, kicks, cooldowns and important spells across frames, nameplates, portraits and alerts.",
         features=[
             "Enemy CC displayed on party and raid frames",
             "Active cooldowns shown on party and raid frames",
             "Important spells and defensives on nameplates and portraits",
             "Enemy and ally kick timers",
             "Party PvP trinket tracking",
             "Warns you when your healer is in CC",
             "Custom aura icon alerts with sound",
             "Supports ElvUI, Danders Frames, Ellesmere Frames and more",
             "Available in 10 languages",
         ]),
    dict(name="MiniClassColors", icon="MiniClassColors.svg", cf=1418767, gh="mini-class-colors",
         tags=["frames"], flavors=["Retail", "Classic"],
         tagline="Applies class colors to the target, focus and target-of-target frames.",
         features=[
             "Class colors the target, focus and target-of-target frames",
             "Identify an enemy's class at a glance",
         ]),
    dict(name="MiniCombatNotifier", icon="MiniCombatNotifier.svg", cf=1421099, gh="mini-combat-notifier",
         tags=["qol"], flavors=["Retail", "Classic"],
         tagline="Notifies you when entering and leaving combat.",
         features=[
             "Shows text on screen when entering and leaving combat",
             "A calmer alternative to Blizzard's scrolling combat text",
         ]),
    dict(name="MiniCompactRunes", icon="MiniCompactRunes.svg", cf=1418878, gh="mini-compact-runes",
         tags=["class"], flavors=["Retail", "Classic"],
         tagline="Tracks runic power and rune cooldowns in a simple, compact display.",
         features=[
             "Runes and runic power in one small display",
             "Position it near the centre of your UI",
             "Suits a flat, modern UI style",
         ]),
    dict(name="MiniDruidMana", icon="MiniDruidMana.svg", cf=1420386, gh="mini-druid-mana",
         tags=["class"], flavors=["Retail", "Classic"],
         tagline="Shows a mana bar while in cat, bear or boomkin form.",
         features=[
             "Know when to stop drinking while stealthed",
             "In Classic, see whether you can afford to shift out and back",
             "As feral or boomie, know if you have mana for off heals",
         ]),
    dict(name="MiniFader", icon="MiniFader.svg", cf=1420477, gh="mini-fader",
         tags=["ui"], flavors=["Retail"],
         tagline="Fades out UI frames until you mouse over them, for a cleaner minimalist look.",
         features=[
             "Bags bar and micro menu",
             "Objective and quest tracker",
             "Raid manager flyout",
             "XP and reputation bars",
             "Chat tabs and icons",
             "Blizzard's damage meters",
         ]),
    dict(name="MiniGoldSync", icon="MiniGoldSync.svg", cf=1421203, gh="mini-gold-sync",
         tags=["qol"], flavors=["Retail"],
         tagline="Automatically balances your gold with the warband bank every time you visit a bank.",
         features=[
             "Set a desired gold amount to maintain across all characters",
             "Per-character override values",
             "Ignore specific characters entirely",
             "Chat messages tell you what was deposited or withdrawn",
         ]),
    dict(name="MiniHealerRange", icon="MiniHealerRange.svg", cf=1429245, gh="mini-healer-range",
         tags=["qol", "pvp"], flavors=["Retail", "Classic"],
         tagline="Warns you when you're out of range of your healer.",
         features=[
             "Simple big red text when you're out of healer range",
             "Helps you keep good positioning in combat",
         ]),
    dict(name="MiniHealthNumbers", icon="MiniHealthNumbers.svg", cf=1434957, gh="mini-health-numbers",
         tags=["frames"], flavors=["Classic"],
         tagline="Shows real health values of mobs and players instead of percentages.",
         features=[
             "Real health values for mobs",
             "Estimates player health from combat log events",
         ]),
    dict(name="MiniHider", icon="MiniHider.svg", cf=1420904, gh="mini-hider",
         tags=["ui"], flavors=["Retail"],
         tagline="Hides UI frames you don't need, for a cleaner interface.",
         features=[
             "Resting zzz and its flashing animation",
             "Prestige badges, corner icon and level text",
             "Blizzard arena frames and frame titles",
             "Bags bar, micro menu and social icon",
             "Stance bar",
             "Hotkey text on action bars",
         ]),
    dict(name="MiniHonorCapped", icon="MiniHonorCapped.svg", cf=1418708, gh="mini-honor-capped",
         tags=["pvp", "qol"], flavors=["Retail", "Classic"],
         tagline="Warns you in chat when you're almost honor capped.",
         features=[
             "Prints a chat message before you waste honor at the cap",
         ]),
    dict(name="MiniHotKeysHider", icon="MiniHotKeysHider.svg", cf=1419310, gh="mini-hotkeys-hider",
         tags=["ui"], flavors=["Retail", "Classic"],
         tagline="Hides the hotkey text on your action bars for a cleaner look.",
         features=[
             "Removes hotkey text from action bars",
             "Perfect once you've memorised your binds",
         ]),
    dict(name="MiniKillingBlow", icon="MiniKillingBlow.svg", cf=1418796, gh="mini-killing-blow",
         tags=["pvp", "sound"], flavors=["Retail", "Classic"],
         tagline="Plays a sound when you land a killing blow on a player.",
         features=[
             "Triggers on player killing blows only",
             "Sound packs: Unreal Tournament, Halo, Guns, One Gun",
             "Add your own custom sounds",
         ]),
    dict(name="MiniMarkers", icon="MiniMarkers.svg", cf=1418841, gh="mini-markers",
         tags=["frames"], flavors=["Retail", "Classic"],
         tagline="Puts spec, class, role or texture markers above nameplates.",
         features=[
             "Show icons for everyone, or just your group",
             "High quality class and spec icons",
             "Role icons for tank, healer and dps",
             "Special icon for Battle.net friends and guild members",
             "Use any texture, with optional class colouring",
             "Works with nameplate addons such as Plater and Platynator",
         ]),
    dict(name="MiniMeter", icon="MiniMeter.svg", cf=1419348, gh="mini-meter",
         tags=["qol"], flavors=["Retail", "Classic"],
         tagline="Shows FPS and ping on your UI.",
         features=[
             "FPS and ping always visible on screen",
             "Drag the text anywhere you like",
         ]),
    dict(name="MiniMythicKeys", icon="MiniMythicKeys.svg", cf=1418981, gh="mini-mythic-keys",
         tags=["qol"], flavors=["Retail"],
         tagline="Answers !key requests in chat and shows all party and guild keystones.",
         features=[
             "Responds to !key and !keys in party, raid and guild chat",
             "/keys opens a window listing everyone's keystones",
             "No more digging through your bags for your key",
         ]),
    dict(name="MiniNameplatePower", icon="MiniNameplatePower.svg", cf=None, gh="mini-nameplate-power",
         tags=["class", "frames"], flavors=["Retail", "Classic"],
         tagline="Tracks runic power on the targeted nameplate.",
         features=[
             "Displays runic power right on your target's nameplate",
         ]),
    dict(name="MiniOvershields", icon="MiniOvershields.svg", cf=1429179, gh="mini-overshields",
         tags=["frames"], flavors=["Retail", "Classic"],
         tagline="Shows overshields and absorbs on unit, player and target frames.",
         features=[
             "Overshield and absorb bars on unit frames",
             "Monitor shield overabsorption as a Disc priest",
             "Track Ignore Pain as a Prot warrior",
             "Works with mage barriers",
         ]),
    dict(name="MiniPressRelease", icon="MiniPressRelease.svg", cf=1427615, gh="mini-press-release",
         tags=["qol"], flavors=["Retail", "Classic"],
         tagline="Makes keys and mouse clicks trigger actions on both press and release.",
         features=[
             "Actions fire on both key down and key up",
             "Increases your chance of landing spammed abilities like Kick",
             "Mouse support for one-handed gaming",
             "An accessibility option for players with disabilities",
         ]),
    dict(name="MiniQueueTimer", icon="MiniQueueTimer.svg", cf=1418678, gh="mini-queue-timer",
         tags=["qol", "pvp"], flavors=["Retail", "Classic"],
         tagline="Shows the elapsed time of your longest PvP or PvE queue on screen.",
         features=[
             "Always-visible elapsed queue timer",
             "Works for both PvP and PvE queues",
         ]),
    dict(name="MiniRangeFader", icon="MiniRangeFader.svg", cf=1447128, gh="mini-range-fader",
         tags=["frames"], flavors=["Retail"],
         tagline="Customises raid frame transparency for units out of range.",
         features=[
             "Set your own out-of-range transparency value",
             "Counteracts the aggressive Midnight transparency changes",
         ]),
    dict(name="MiniResourceDisplay", icon="MiniResourceDisplay.svg", cf=1418734, gh="mini-resource-display",
         tags=["frames"], flavors=["Retail", "Classic"],
         tagline="A simple personal resource-style health and power bar you can tweak.",
         features=[
             "Like Blizzard's personal resource bar, with additions",
             "Shows text values of your health and power",
             "Move, resize and scale it freely",
         ]),
    dict(name="MiniRoleIcons", icon="MiniRoleIcons.svg", cf=1422921, gh="mini-role-icons",
         tags=["frames"], flavors=["Retail", "Classic"],
         tagline="Replaces the role icons on unit frames.",
         features=[
             "Custom high quality role icons",
             "Custom sizing and class colouring",
             "Supports Shadowed Unit Frames",
         ]),
    dict(name="MiniSurrender", icon="MiniSurrender.svg", cf=1419004, gh="mini-surrender",
         tags=["pvp", "qol"], flavors=["Retail", "Classic"],
         tagline="Type /afk or /gg to surrender arena.",
         features=[
             "Surrender instantly with /afk or /gg",
             "No PvP icon right-click, no confirm popup",
         ]),
    dict(name="MiniTabTarget", icon="MiniTabTarget.svg", cf=1418962, gh="mini-tab-target",
         tags=["pvp", "qol"], flavors=["Retail", "Classic"],
         tagline="Swaps tab targeting to nearest player in PvP and nearest enemy in PvE.",
         features=[
             "Automatically switches tab behaviour between PvP and PvE",
             "No more manually changing keybindings",
             "Detects your target enemy keybindings automatically",
         ]),
    dict(name="MiniTotemCancel", icon="MiniTotemCancel.svg", cf=1418690, gh="mini-totem-cancel",
         tags=["class", "pvp"], flavors=["Retail", "Classic"],
         tagline="Creates buttons for use in macros to cancel totems.",
         features=[
             "Four macro buttons for cancelling totems",
             "Destroy active totems with a single macro",
         ]),
    dict(name="MiniTrinketGlow", icon="MiniTrinketGlow.svg", cf=1425196, gh="mini-trinket-glow",
         tags=["pvp", "qol"], flavors=["Retail", "Classic"],
         tagline="Glows trinkets on your action bars when they come off cooldown.",
         features=[
             "Works no matter which action slot your trinket is in",
             "Combat-only toggle option",
             "Supports /use 13 and /use 14 macros",
         ]),
    dict(name="MiniWinLoss", icon="MiniWinLoss.svg", cf=1419503, gh="mini-win-loss",
         tags=["pvp"], flavors=["Retail", "Classic"],
         tagline="Shows your rated PvP win-loss record on the conquest frame.",
         features=[
             "Win-loss ratios and percentages for every rated bracket",
             "Covers 2v2, 3v3, solo shuffle, blitz and rated battlegrounds",
         ]),
    dict(name="RoosterLoop", icon="RoosterLoop.png", cf=1418786, gh="rooster-loop",
         tags=["sound"], flavors=["Retail", "Classic"],
         tagline="Plays the Robin Hood rooster whistle song on conditions of your choosing.",
         features=[
             "The legendary rooster whistle, in Azeroth",
             "Configurable triggers: walking, standing still, flying and more",
         ]),
]

FEATURED = {
    "FrameSort": "https://raw.githubusercontent.com/Verubato/framesort/main/assets/Screenshots/3v3SortingTop.png",
    "MiniAuras": "https://raw.githubusercontent.com/Verubato/mini-auras/main/assets/Screenshots/TestFrames.png",
    "RoosterLoop": "https://raw.githubusercontent.com/Verubato/rooster-loop/main/assets/Screenshots/Rooster.gif",
}

TAG_LABELS = {
    "pvp": "PvP",
    "frames": "Frames",
    "ui": "UI Cleanup",
    "qol": "QoL",
    "class": "Class Tools",
    "sound": "Sounds",
}

CHIPS = [
    ("all", "All"),
    ("pvp", "PvP & Arena"),
    ("frames", "Frames & Nameplates"),
    ("ui", "UI Cleanup"),
    ("qol", "Quality of Life"),
    ("class", "Class Tools"),
    ("sound", "Sounds & Fun"),
]

e = html.escape


def links_html(a):
    parts = []
    if a["cf"]:
        parts.append('<a href="https://www.curseforge.com/projects/%d" target="_blank" rel="noopener">CurseForge</a>' % a["cf"])
    parts.append('<a href="https://github.com/Verubato/%s" target="_blank" rel="noopener">GitHub</a>' % a["gh"])
    return "\n          ".join(parts)


def card_html(a):
    tags = " ".join(a["tags"])
    tag_pills = "".join('<span class="tag">%s</span>' % e(TAG_LABELS[t]) for t in a["tags"])
    flavor_pills = "".join('<span class="tag">%s</span>' % e(f) for f in a["flavors"])
    feats = "\n            ".join("<li>%s</li>" % e(f) for f in a["features"])
    return f'''      <article class="addon-card" data-tags="{tags}">
        <div class="head">
          <img src="assets/icons/{a["icon"]}" alt="" loading="lazy" width="44" height="44">
          <div>
            <h3>{e(a["name"])}</h3>
            <div class="tags">{tag_pills}{flavor_pills}</div>
          </div>
        </div>
        <p class="tagline">{e(a["tagline"])}</p>
        <details>
          <summary>Features</summary>
          <ul>
            {feats}
          </ul>
        </details>
        <div class="links">
          {links_html(a)}
        </div>
      </article>'''


def featured_html(a):
    feats = "\n            ".join("<li>%s</li>" % e(f) for f in a["features"][:6])
    btns = []
    if a["cf"]:
        btns.append('<a class="btn primary" href="https://www.curseforge.com/projects/%d" target="_blank" rel="noopener">Download on CurseForge</a>' % a["cf"])
    btns.append('<a class="btn" href="https://github.com/Verubato/%s" target="_blank" rel="noopener">View on GitHub</a>' % a["gh"])
    btns = "\n            ".join(btns)
    return f'''      <article class="featured-card">
        <div class="featured-body">
          <div class="head">
            <img src="assets/icons/{a["icon"]}" alt="" width="52" height="52">
            <h3>{e(a["name"])}</h3>
          </div>
          <p class="tagline">{e(a["tagline"])}</p>
          <ul>
            {feats}
          </ul>
          <div class="links">
            {btns}
          </div>
        </div>
        <div class="featured-media">
          <img src="{FEATURED[a["name"]]}" alt="{e(a["name"])} screenshot" loading="lazy">
        </div>
      </article>'''


featured_cards = "\n".join(featured_html(a) for a in ADDONS if a["name"] in FEATURED)
cards = "\n".join(card_html(a) for a in ADDONS)
chips = "\n        ".join(
    '<button class="chip%s" data-tag="%s">%s</button>' % (" active" if k == "all" else "", k, e(label))
    for k, label in CHIPS
)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Verz Addons &ndash; Lightweight World of Warcraft Addons</title>
  <meta name="description" content="{len(ADDONS)} World of Warcraft addons by Verz: FrameSort, MiniAuras, the Mini suite and more. Lightweight, focused addons for PvP, unit frames and UI cleanup.">
  <meta name="theme-color" content="#0f1012">
  <link rel="canonical" href="https://verzaddons.com/">
  <meta property="og:title" content="Verz Addons &ndash; Lightweight World of Warcraft Addons">
  <meta property="og:description" content="{len(ADDONS)} WoW addons: FrameSort, MiniAuras, the Mini suite and more. Lightweight, focused addons for PvP, unit frames and UI cleanup.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://verzaddons.com/">
  <meta property="og:site_name" content="Verz Addons">
  <meta property="og:image" content="https://verzaddons.com/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Verz Addons: lightweight addons for World of Warcraft">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Verz Addons &ndash; Lightweight World of Warcraft Addons">
  <meta name="twitter:description" content="{len(ADDONS)} WoW addons: FrameSort, MiniAuras, the Mini suite and more.">
  <meta name="twitter:image" content="https://verzaddons.com/assets/og-image.png">
  <link rel="icon" type="image/svg+xml" href="assets/logo.svg">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header class="site-header">
    <div class="container">
      <img class="logo" src="assets/logo.svg" alt="">
      <a class="brand" href="#">Verz Addons</a>
      <nav>
        <a href="#featured">Featured</a>
        <a href="#addons">All Addons</a>
        <a class="hide-mobile" href="https://github.com/Verubato" target="_blank" rel="noopener">GitHub</a>
      </nav>
    </div>
  </header>

  <section class="hero">
    <img class="logo" src="assets/logo.svg" alt="Verz Addons logo">
    <h1>Lightweight addons for <span class="accent">World of Warcraft</span></h1>
    <p class="tagline">Small, focused, performance-friendly addons that each do one thing well. From frame sorting and PvP aura tracking to tiny quality-of-life fixes.</p>
    <div class="stats">
      <div class="stat"><span class="num">{len(ADDONS)}</span><span class="label">Addons</span></div>
    </div>
    <div class="actions">
      <a class="btn primary" href="#addons">Browse the addons</a>
      <a class="btn" href="https://github.com/Verubato" target="_blank" rel="noopener">GitHub</a>
    </div>
  </section>

  <section id="featured">
    <div class="container">
      <h2 class="section-title">Featured</h2>
      <p class="section-sub">The big ones. Battle-tested addons with deep feature sets.</p>
      <div class="featured-grid">
{featured_cards}
      </div>
    </div>
  </section>

  <section id="addons">
    <div class="container">
      <h2 class="section-title">All addons</h2>
      <p class="section-sub">Every addon is standalone. Install only what you want; none of them depend on each other.</p>
      <div class="filter-bar">
        <input id="addon-search" type="search" placeholder="Search addons..." aria-label="Search addons">
        {chips}
      </div>
      <div class="addon-grid">
{cards}
      </div>
      <p id="no-results" class="no-results">No addons match your search.</p>
    </div>
  </section>

  <footer class="site-footer">
    <div class="container">
      <div>Made by Verz.</div>
      <div><a href="https://github.com/Verubato" target="_blank" rel="noopener">GitHub</a></div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
'''

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "index.html")
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(page)

print("wrote index.html with %d addons" % len(ADDONS))
