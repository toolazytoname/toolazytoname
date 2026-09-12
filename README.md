# Hi, I'm lazy 👋 (懒得起名)

**Ex-big-tech infra engineer, now an indie dev with ski/climbing/swim instructor certs.**

📍 Beijing · 🛠️ Building tools I actually use, with AI · ⛷️🧗🏊 Ski / climbing / swim instructor

At a leading tech company I built the industry's first in-house **Swift compilation cache** (cut build times by 50%, served 71% of all company builds) and an **LLVM-based iOS privacy-scanning toolchain**, with 4 patents. Now I ship my own tools.

Recent work also lives on **[LazyOS](https://lazyos.weichao.studio)** ([repo](https://github.com/toolazytoname/lazyos)).

![Swift](https://img.shields.io/badge/-Swift-FA7343?style=flat-square&logo=swift&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Objective-C](https://img.shields.io/badge/-Objective--C-438EFF?style=flat-square&logo=apple&logoColor=white)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![Claude Code](https://img.shields.io/badge/-Claude%20Code-121212?style=flat-square&logo=anthropic&logoColor=white)
![Grok](https://img.shields.io/badge/-Grok-000000?style=flat-square&logo=x&logoColor=white)

---

## 📱 Mobile Lab & On-Device AI

- 🔬 **[oneplus-8t-mobile-lab](https://github.com/toolazytoname/oneplus-8t-mobile-lab)** — An open phone lab grown out of one OnePlus 8T: Android flashing & recovery, real-device automation, authorized mobile security, wireless observation, and on-device AI agents. · [guide](https://toolazytoname.github.io/oneplus-8t-mobile-lab/)
- 🤖 **[android-ai-stack](https://github.com/toolazytoname/android-ai-stack)** — A local-first AI toolchain for an Android phone running Termux + Kali PRoot: OpenCode, Claude Code, Happy's agent and server all run on the phone.
- 📞 **[xiaohei-phone-agent](https://github.com/toolazytoname/xiaohei-phone-agent)** — "Wake it. Say it. Let your phone act." An open, local-first AI phone assistant for Android — voice command → intent routing → observable actions, with confirmation when it matters.
- 🕵️ **[pocket-pentest](https://github.com/toolazytoname/pocket-pentest)** — Turn an Android phone into an authorized pentest / CTF carry-on toolkit. No custom kernel, no system downgrade — Magisk root + Termux/PRoot Kali userspace.
- 🧪 **[android-device-test](https://github.com/toolazytoname/android-device-test)** — Real-device Android testing skill: ADB triage, state pinning, uiautomator2, PerfDog, monkey — and telling real failures from false ones.

## 🤖 Agents & Automation

- 🤵 **[GridGo · 格行](https://github.com/toolazytoname/GridGo)** — A personal Agent butler — one grid, one task.
- 📊 **[llm-quota-watchdog](https://github.com/toolazytoname/llm-quota-watchdog)** — One dashboard + smart push alerts for LLM coding-plan quotas — Claude Pro/Max, Codex Plus/Pro, Kimi for Coding, GLM Coding Plan. Python stdlib only, static HTML, no DB. · [live](https://quota.weichao.studio)
- 🔀 **[tokenlane](https://github.com/toolazytoname/tokenlane)** — Local-first Claude Code provider switcher. `lane use glm` and go; tokens stay on disk.
- 📡 **[happy-relay-deploy](https://github.com/toolazytoname/happy-relay-deploy)** — A skill for self-hosting a Happy relay when you genuinely need to drive Claude Code on a remote machine from your phone. Tailnet-only by default.
- 🛰️ **[paseo-relay-deploy](https://github.com/toolazytoname/paseo-relay-deploy)** — A skill to self-host a Paseo WebSocket relay — the phone app drives multiple machines without opening Tailscale.
- 🧠 **[dsh-deploy](https://github.com/toolazytoname/dsh-deploy)** — A skill to deploy DeepSeek Harness (`dsh web`) behind nginx + Tailscale Funnel, with Safari cookie auth and remote Settings patches.
- 📱 **[dsh-ios](https://github.com/toolazytoname/dsh-ios)** — Unofficial iOS companion for DeepSeek Harness — same sessions as the web UI. Not a DeepSeek product.

## 🔧 Infra & Ops Skills

- 🖥️ **[Lodge](https://github.com/toolazytoname/lodge)** — See every service running on each of your servers, what's exposed where — hub + agent architecture, a single Go binary, E2E-encrypted vault. No more spreadsheets that go stale in a week.
- 🏠 **[home-nas-skill](https://github.com/toolazytoname/home-nas-skill)** — Home NAS build & ops playbook: full media pipeline (Prowlarr→Sonarr/Radarr→qB→Bazarr→Jellyfin), Immich, Navidrome, backups — with all the China-network and weak-CPU gotchas baked in.
- 🌐 **[reality-handshake](https://github.com/toolazytoname/reality-handshake)** — Diagnosing VLESS+Reality / XTLS proxy handshake failures, and connecting new clients to an existing server.
- 💬 **[wechat-mp-devops](https://github.com/toolazytoname/wechat-mp-devops)** — WeChat MiniProgram CI/CD & DevOps playbooks (build / upload / scan-test on Linux & macOS), packaged as a drop-in skill.
- 🛒 **[cn-electronics-shop](https://github.com/toolazytoname/cn-electronics-shop)** — 国内数码选购顾问 Skill：拆需求、京东/天猫/闲鱼比价、验闲鱼、叠国补和大促. Decision layer only — it does not crawl or place orders.

## 📓 Archives & Field Notes

- 💾 **[wechat-local-archive](https://github.com/toolazytoname/wechat-local-archive)** — Local macOS WeChat archive: decrypt the live DB, export JSONL / Markdown / HTML, browse on 127.0.0.1.
- 📓 **[yinxiang-export](https://github.com/toolazytoname/yinxiang-export)** — Archive-first Yinxiang local export: originals preserved, Markdown reading layer, Agent Skill.
- 📖 **[kindle-field-guide](https://github.com/toolazytoname/kindle-field-guide)** — Two old Kindles, documented for daily use and safe maintenance. · [guide](https://toolazytoname.github.io/kindle-field-guide/)
- 🔧 **[pocket-lab](https://github.com/toolazytoname/pocket-lab)** — 口袋实验室 — a hardware handbook for programmers: radio, watches, pocket computers, vision, robots. · [guide](https://toolazytoname.github.io/pocket-lab/)

## 🧩 Standalone Projects

- 🐰 **[小兔头节拍器](https://jpq.weichao.studio)** — A metronome that opens right in your browser — kid-voice beat counting, traditional strong/weak beats, multiple time signatures. For piano, drums, or dance practice. · [repo](https://github.com/toolazytoname/metronome)
- 🏭 **[MediaForge](https://github.com/toolazytoname/MediaForge)** — An AI self-media pipeline: topic selection → creation (article/video) → quality gate → human review → scheduled multi-platform publishing → analytics feedback. Quality comes from the veto — it dares to drop 70% of output.
- 🦆 **[AquaSight · 鸭先知](https://github.com/toolazytoname/AquaSight)** — A personal news radar: scheduled ingest, clustering, Chinese digest, Bark, and a web reader.
- 🗣️ **[DigitalHuman](https://github.com/toolazytoname/DigitalHuman)** — Local talking-head on Apple Silicon: a face video + audio → lip-synced mp4. LatentSync 1.5 + MPS, no NVIDIA.
- 🛡️ **[Sentinel](https://github.com/toolazytoname/Sentinel)** — A disciplined cryptocurrency quantitative system for the long-term investor. Its value isn't "earning more" — it's using machine-level discipline to stop you from repeating your own mistakes. LLM only does research / review / veto; it never places orders.
- 📡 **On-chain (read-only)** — no keys, no orders, no custody: [paysentry](https://github.com/toolazytoname/paysentry) · [hlsentry](https://github.com/toolazytoname/hlsentry) · [oddsradar](https://github.com/toolazytoname/oddsradar) · [chaintail](https://github.com/toolazytoname/chaintail) · [slotbench](https://github.com/toolazytoname/slotbench)

## 📜 Legacy iOS

- 💬 **[WeChatExport](https://github.com/toolazytoname/WeChatExport)** — Export WeChat chat logs (iOS). Current Mac path is [wechat-local-archive](https://github.com/toolazytoname/wechat-local-archive).
- 🏷️ **[FDTops](https://github.com/toolazytoname/FDTops)** — Batch add/replace class-name prefixes — an Xcode helper.
- 🐦 **[BPFlutter](https://github.com/toolazytoname/BPFlutter)** — Flutter integration guide & sample for iOS projects.

## 🆕 Recently shipped

<!-- recently-shipped:start -->
_Public original repos from the last 90 days that aren't listed above. Last refresh: 2026-09-12._

- `2026-08-31` **[mindstorms-51515](https://github.com/toolazytoname/mindstorms-51515)** — 51515 Charlie 玩机手册 · LEGO MINDSTORMS Robot Inventor field notes
- `2026-08-25` **[kazike](https://github.com/toolazytoname/kazike)** — 数字生命卡兹克知识地图
- `2026-08-19` **[x402-stall](https://github.com/toolazytoname/x402-stall)** — Pay-per-request x402 stall for data from sibling tools. Cash register, not a protocol company.
- `2026-08-19` **[bountydesk](https://github.com/toolazytoname/bountydesk)** — Personal desk for ecosystem bounties, RFPs, and small paid tasks. Cash plugin, not a product company.
- `2026-08-18` **[PixelDen](https://github.com/toolazytoname/PixelDen)** — Pixel art den — small image tools and experiments.
- `2026-08-17` **[dsh-plugin-grok](https://github.com/toolazytoname/dsh-plugin-grok)** — DeepSeek Harness plugin: drive the local Grok Build CLI for text, image, and video.
- `2026-08-14` **[grok-imagine-on-plan](https://github.com/toolazytoname/grok-imagine-on-plan)** — Agent skill: generate images and videos on SuperGrok/Grok coding-plan quota via Grok Build tools
<!-- recently-shipped:end -->

---

## ✍️ Writing

- Blog: [weichao.ren](https://www.weichao.ren/) — build systems, indie hacking, and everything in between.

<details>
<summary>Off-screen</summary>

- ⛷️ Ski instructor (alpine + snowboard)
- 🧗 Rock climbing instructor
- 🏊 Swim instructor
- 🤿 PADI Advanced Open Water Diver
- 🩺 Red Cross first-aider
- Coding and sports share one thing: the joy of getting better at something real.

</details>

## 📫 Connect

[![Blog](https://img.shields.io/badge/-weichao.ren-000000?style=flat-square&logo=google-chrome&logoColor=white)](https://www.weichao.ren/)
[![Email](https://img.shields.io/badge/-lazywc@gmail.com-000000?style=flat-square&logo=gmail&logoColor=white)](mailto:lazywc@gmail.com)
