# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the app, no matter what number I typed — even 1, the lowest possible — the hint always said "Go LOWER!", making it impossible to make progress. The game was fundamentally unplayable. Two concrete bugs I noticed immediately: first, the hints were always wrong regardless of the guess; second, after losing a round and clicking "New Game," the game appeared to reset (the attempt count refreshed) but submitting a new guess did nothing — the game was silently frozen.

---

## 2. How did you use AI as a teammate?

I used Claude Code (Anthropic) as my AI assistant throughout this project. One example of a correct suggestion: when I described the "always Go Lower" symptom, the AI correctly identified that `secret` was being cast to a string on even-numbered attempts, causing Python's lexicographic string comparison to produce wrong results — I verified this by checking the Developer Debug Info panel, which showed the secret as an integer, while the comparison was treating it as a string. One example where I had to stay in control: the AI initially suggested using `st.empty()` to fix the attempts display timing issue, which was a valid fix, but I rejected an earlier plan-mode proposal that would have restructured the UI layout more than necessary — I approved only the minimal targeted change.

---

## 3. Debugging and testing your fixes

I verified each fix by manually playing the game immediately after applying it — for example, after fixing the hint logic I tested with a number I knew was above the secret (from the debug panel) and confirmed it now said "Go LOWER!" correctly. I also ran `pytest tests/test_game_logic.py -v` after implementing `logic_utils.py`, which showed all 7 tests passing, confirming that `check_guess` and `get_range_for_difficulty` behaved correctly for boundary cases. The AI helped design the range tests by suggesting patching `random.randint` to return the boundary value `high`, which made it easy to assert the secret stayed within the valid range without relying on randomness.

---

## 4. What did you learn about Streamlit and state?

In the original app, the secret number was generated with `random.randint(low, high)` at the top level of the script — outside of `st.session_state`. Every time a user clicked a button, Streamlit re-ran the entire script from top to bottom, generating a new random secret each time. Streamlit "reruns" means the whole Python file executes fresh on every user interaction, like reloading a page; `st.session_state` is a dictionary that persists between those reruns so values aren't lost. The fix was wrapping the secret generation in `if "secret" not in st.session_state:`, so it only generates once and stores it across reruns.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is checking the rendering order of UI elements when using frameworks like Streamlit — the attempts display bug taught me that where you place a widget in the script matters because it determines what value it reads at render time. Next time I work with AI on a coding task, I would ask it to explain why a bug exists before accepting a fix, rather than just applying the change — understanding the root cause helped me catch cases where the suggested fix was overly broad. This project changed how I think about AI-generated code: it can introduce subtle, hard-to-spot bugs that look correct on the surface, so treating AI output as a first draft that needs human review and testing is essential.

---
