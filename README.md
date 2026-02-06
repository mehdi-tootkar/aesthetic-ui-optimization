# Aesthetic UI Optimization

## Overview
This repository contains a research-oriented system for the automatic aesthetic optimization of web UI mockups.
The project investigates how reinforcement learning and black-box aesthetic evaluation models can be combined
to iteratively improve the visual quality of UI designs without human-in-the-loop feedback.

The system operates on rendered UI images (e.g., exported from Figma) and applies controlled, parameterized
design modifications such as spacing, alignment, and layout adjustments.

---

## Research Context
- Title: AI-Driven Aesthetic Optimization of Web UI Mockups
- Year: 2025
- Role: Research Assistant
- Supervisor: Dr. Shiva Kamkar

---

## Core Contributions
- Formulation of UI redesign as a Markov Decision Process (MDP)
- Integration of a black-box aesthetic evaluation model as a reward signal
- Modular client–server architecture separating design tools from optimization logic
- Custom Gymnasium environment for learning-based optimization
- FastAPI-based service layer for scalable evaluation

---

## System Architecture
The system consists of the following components:

- Design Environment: Figma (via plugin)
- Service Layer: FastAPI
- Evaluator: Aesthetic scoring model (black-box)
- Optimization Core: Gymnasium environment

---

## Repository Structure
```
aesthetic-ui-optimization/
├── server/
│   ├── main.py
│   ├── schemas.py
│   ├── evaluator/
│   │   └── aesthetic.py
│   └── env/
│       └── aesthetic_env.py
│
├── figma-plugin/
│   ├── manifest.json
│   ├── code.js
│   └── ui.html
│
├── docs/
├── run_env.py
├── test_scorer.py
├── ui_test.png
└── requirements.txt
```

---

## Installation
```
conda create -n aesthetic python=3.10 -y
conda activate aesthetic
pip install -r requirements.txt
pip install fastapi uvicorn requests gymnasium
```

---

## Usage
```
uvicorn server.main:app --reload
python test_scorer.py
python run_env.py
```

---

## Method Summary
- State: Structured UI representation
- Action: Discrete UI modifications
- Reward: Difference in aesthetic score
- Objective: Maximize cumulative improvement

---

## Project Status
- Aesthetic evaluator integrated
- FastAPI service operational
- Gymnasium environment implemented
- Figma plugin integration in progress

---

## Contact
https://github.com/USERNAME/aesthetic-ui-optimization
