# Hi, I'm lazy 👋 (懒得起名)

**Ex-big-tech infra engineer, now an indie dev with ski/climbing/swim instructor certs.**

📍 Beijing · 🛠️ Building tools I actually use, with AI · ⛷️🧗🏊 Ski / climbing / swim instructor

At a leading tech company I built the industry's first in-house **Swift compilation cache** (cut build times by 50%, served 71% of all company builds) and an **LLVM-based iOS privacy-scanning toolchain**, with 4 patents. Now I ship my own tools.

![Swift](https://img.shields.io/badge/-Swift-FA7343?style=flat-square&logo=swift&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Objective-C](https://img.shields.io/badge/-Objective--C-438EFF?style=flat-square&logo=apple&logoColor=white)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![Claude Code](https://img.shields.io/badge/-Claude%20Code-121212?style=flat-square&logo=anthropic&logoColor=white)

---

## 🚀 Products (live)

| | | |
|---|---|---|
| 🐰 **[小兔头节拍器](https://jpq.weichao.studio)** | A metronome that opens right in your browser — kid-voice beat counting, traditional strong/weak beats, multiple time signatures. For piano, drums, or dance practice. | [repo](https://github.com/toolazytoname/metronome) · WeChat Mini Program |
| 🤵 **GridGo · 格行** | A personal Agent butler — one grid, one task. | [repo](https://github.com/toolazytoname/GridGo) · in beta |
| 🖥️ **Lodge** | See every service running on each of your servers, what's exposed where — hub + agent architecture, a single Go binary, E2E-encrypted vault. No more spreadsheets that go stale in a week. | [repo](https://github.com/toolazytoname/lodge) |

## 🤖 AI Dev Stack & Agent Harness

- 🧪 **[autodev-harness](https://github.com/toolazytoname/autodev-harness)** — AI-driven development harness with independent quality loops. The model is the cheapest part — quality comes from the structure (generate → independent reviewers → gate → commit). Say one sentence, walk away, come back to a high-quality result.
- 🖥️ **[atelier](https://github.com/toolazytoname/atelier)** — macOS + Claude Code, isolated in a disposable Linux VM. Your host stays clean.
- 🤖 **[android-ai-stack](https://github.com/toolazytoname/android-ai-stack)** — A local-first AI toolchain for an Android phone running Termux + Kali PRoot: OpenCode, Claude Code, Happy's agent and server all run on the phone.
- 📊 **[llm-quota-watchdog](https://github.com/toolazytoname/llm-quota-watchdog)** — One dashboard + smart push alerts for LLM coding-plan quotas — Claude Pro/Max, Codex Plus/Pro, Kimi for Coding, GLM Coding Plan. Python stdlib only, static HTML, no DB.
- 📡 **[happy-relay-deploy](https://github.com/toolazytoname/happy-relay-deploy)** — A skill for self-hosting a Happy relay when you genuinely need to drive Claude Code on a remote machine from your phone. Tailnet-only by default.

## 📱 Mobile Lab & Security Research

- 🔬 **[oneplus-8t-mobile-lab](https://github.com/toolazytoname/oneplus-8t-mobile-lab)** — An open phone lab grown out of one OnePlus 8T: Android flashing & recovery, real-device automation, authorized mobile security, wireless observation, and on-device AI agents.
- 🕵️ **[pocket-pentest](https://github.com/toolazytoname/pocket-pentest)** — Turn an Android phone into an authorized pentest / CTF carry-on toolkit. No custom kernel, no system downgrade — Magisk root + Termux/PRoot Kali userspace.
- 📞 **[xiaohei-phone-agent](https://github.com/toolazytoname/xiaohei-phone-agent)** — "Wake it. Say it. Let your phone act." An open, local-first AI phone assistant for Android — voice command → intent routing → observable actions, with confirmation when it matters.
- 🧪 **[android-device-test](https://github.com/toolazytoname/android-device-test)** — Real-device Android testing skill: ADB triage, state pinning, uiautomator2, PerfDog, monkey — and telling real failures from false ones.
- 🔐 **[relay-proxy](https://github.com/toolazytoname/relay-proxy)** — Let an AI agent operate your Linux servers without handing it the password. The agent only talks to a relay; the relay uses temporary, revocable credentials.

## 🔧 Self-Hosted & Ops Skills

- 🏠 **[home-nas-skill](https://github.com/toolazytoname/home-nas-skill)** — Home NAS build & ops playbook as a Claude Code skill: full media pipeline (Prowlarr→Sonarr/Radarr→qB→Bazarr→Jellyfin), Immich, Navidrome, backups — with all the China-network and weak-CPU gotchas baked in.
- 🌐 **[reality-handshake](https://github.com/toolazytoname/reality-handshake)** — Diagnosing VLESS+Reality / XTLS proxy handshake failures, and connecting new clients to an existing server.
- 💬 **[wechat-mp-devops](https://github.com/toolazytoname/wechat-mp-devops)** — WeChat MiniProgram CI/CD & DevOps playbooks (build / upload / scan-test on Linux & macOS), packaged as a drop-in Claude Code skill.

## 🎬 Media & Content

- 🏭 **[MediaForge](https://github.com/toolazytoname/MediaForge)** — An AI self-media pipeline: topic selection → creation (article/video) → quality gate → human review → scheduled multi-platform publishing → analytics feedback. Quality comes from the veto — it dares to drop 70% of output.
- 📰 **[self-media-platform](https://github.com/toolazytoname/self-media-platform)** — An AI content creation & multi-platform distribution system. Multi-provider (MiniMax / Claude / OpenAI-compatible) creation center.
- 📨 **[wechat-autopost](https://github.com/toolazytoname/wechat-autopost)** — Auto-scrape trending articles → AI rewrite (keeps the gist, strips the AI smell) → one-click publish to WeChat / Zhihu / Jianshu / CSDN.
- 🧸 **[toys](https://github.com/toolazytoname/toys)** — Personal toys & experiments. [live](https://toys-iota-pearl.vercel.app)

## 📈 Quant Trading

- 🛡️ **[Sentinel](https://github.com/toolazytoname/Sentinel)** — A disciplined cryptocurrency quantitative system for the long-term investor. Its value isn't "earning more" — it's using machine-level discipline to stop you from repeating your own mistakes. LLM only does research / review / veto; it never places orders.

## 📜 Legacy iOS

- 💬 **[WeChatExport](https://github.com/toolazytoname/WeChatExport)** — Export WeChat chat logs (iOS).
- 🏷️ **[FDTops](https://github.com/toolazytoname/FDTops)** — Batch add/replace class-name prefixes — an Xcode helper.
- 🐦 **[BPFlutter](https://github.com/toolazytoname/BPFlutter)** — Flutter integration guide & sample for iOS projects.

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
