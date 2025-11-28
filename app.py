import random
import gradio as gr

MAX_STEPS = 12  # number of step/range boxes to display


# -------------------------
# Stage 1: Generate a List
# -------------------------
def generate_list():
    arr = random.sample(range(1, 50), 12)
    display = f"Random List (Unsorted):\n{arr}"
    return display, arr


# -------------------------
# Stage 2: Run Linear Search with Gamification
# -------------------------
def linear_search_on_state(user_number, user_guess, arr_state, score):

    # If list not generated yet
    if not arr_state:
        return (
            "⚠️ Please click 'Generate List' first.",
            *[""] * MAX_STEPS,
            *[""] * MAX_STEPS,
            "⚠️ No list to search.",
            score
        )

    # Validate target input
    try:
        target = int(user_number)
    except:
        return (
            f"Random List (Unsorted):\n{arr_state}",
            *[""] * MAX_STEPS,
            *[""] * MAX_STEPS,
            "⚠️ Enter a valid integer for the target.",
            score
        )

    # Validate guess input
    try:
        guess = int(user_guess)
    except:
        guess = None

    arr = arr_state[:]
    steps = []
    ranges = []
    found = False

    # Initial full range
    ranges.append(f"Initial list → {arr}")

    found_index = None

    for i, value in enumerate(arr):
        steps.append(f"Check index {i}: value = {value}")

        # Remaining list after each step
        remaining = arr[i+1:] if i + 1 < len(arr) else []
        ranges.append(f"Remaining elements → {remaining}")

        if value == target:
            steps.append(f"✅ Found {target} at index {i}")
            found = True
            found_index = i
            break

    if not found:
        steps.append(f"❌ {target} was not found in the list.")

    # Pad the lists so UI stays aligned
    while len(steps) < MAX_STEPS:
        steps.append("")
    while len(ranges) < MAX_STEPS:
        ranges.append("")

    # -------------------------
    # Gamification Logic
    # -------------------------

    if guess is None:
        gamification_msg = "🎮 No guess provided."
    else:
        if found and guess == found_index:
            score += 1
            gamification_msg = (
                f"🎉 **Correct Guess!** You guessed index {guess}, and the number was found there! "
                f"\n🏆 Score increased to **{score}**."
            )
        elif not found:
            gamification_msg = (
                f"❌ The number was not found, so index guessing didn't apply.\n"
                f"Current Score: **{score}**"
            )
        else:
            gamification_msg = (
                f"❌ **Incorrect Guess.** You guessed index {guess}, "
                f"but the number was found at index {found_index}.\n"
                f"Current Score: **{score}**"
            )

    final_msg = gamification_msg

    list_display = f"Random List (Unsorted):\n{arr}"

    return (
        list_display,
        *steps[:MAX_STEPS],
        *ranges[:MAX_STEPS],
        final_msg,
        score
    )


# -------------------------
# UI
# -------------------------
with gr.Blocks(title="Linear Search Simulator") as demo:

    gr.Markdown(
        """
        # 🔍 Linear Search Simulator — Now with Gamification! 🎮

        **Step 1:** Click **Generate List**  
        **Step 2:** Enter a number to search  
        **Step 3:** Guess which index the number will be at  

        ### Earn 1 point if your guess is correct!  
        """
    )

    arr_state = gr.State([])
    score_state = gr.State(0)

    with gr.Row():
        gen_btn = gr.Button("Generate List 🎲")
        user_number = gr.Number(label="Enter the target number (1–49)", value=1, precision=0)
        user_guess = gr.Number(label="Guess the index (0–11)", value=0, precision=0)
        run_btn = gr.Button("Run Linear Search 🔎", variant="primary")

    list_box = gr.Textbox(label="Generated List", lines=2, interactive=False)

    gr.Markdown("### 🔹 Search Steps (Each Check)")
    step_boxes = [
        gr.Textbox(label=f"Step {i+1}", lines=1, interactive=False)
        for i in range(MAX_STEPS)
    ]

    gr.Markdown("### 🔸 Remaining List After Each Step")
    range_boxes = [
        gr.Textbox(label=f"Remaining {i+1}", lines=1, interactive=False)
        for i in range(MAX_STEPS)
    ]

    result_box = gr.Textbox(label="Final Result (Gamification)", lines=3, interactive=False)
    score_box = gr.Number(label="🎮 Current Score", interactive=False)

    gen_btn.click(
        fn=generate_list,
        inputs=[],
        outputs=[list_box, arr_state],
    )

    run_btn.click(
        fn=linear_search_on_state,
        inputs=[user_number, user_guess, arr_state, score_state],
        outputs=[list_box, *step_boxes, *range_boxes, result_box, score_state],
    )

    score_state.change(
        fn=lambda s: s,
        inputs=score_state,
        outputs=score_box
    )

if __name__ == "__main__":
    demo.launch()