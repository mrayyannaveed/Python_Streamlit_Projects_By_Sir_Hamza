import streamlit as st
import random

# Set up the page
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮"
)

st.title("💭Number Guessing Game")
st.header("Guess a number between 1 and 100", divider="rainbow")
st.markdown("### You have 5 attempts to guess the number")
st.markdown("### Good luck! 🍀")
st.markdown("---")

# Initialize session state variables
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.user_guess = 1  # Store the user's guess in session state

# Display attempts left
def display_attempts_left(attempts):
    st.markdown(f"**Attempts Left:** {5 - attempts}")

# Input for user's guess
user_guess = st.number_input(
    "**Enter your guess:**",
    min_value=1,
    max_value=100,
    step=1,
    value=st.session_state.user_guess,  # Use session state to retain the user's guess
    key=f"guess_{st.session_state.attempts}"  # Unique key for each attempt
)

# Submit button
if st.button("Submit"):
    if st.session_state.game_over:
        st.warning("🚨 The game is over. Please refresh the page to play again.")
    else:
        # Validate the user's guess
        if user_guess == st.session_state.random_number:
            st.success("🎉 Congratulations! You guessed the number!")
            st.balloons()
            st.session_state.game_over = True
        elif user_guess < st.session_state.random_number:
            st.warning("👇 The number is higher than your guess.")
            st.session_state.attempts += 1
        elif user_guess > st.session_state.random_number:
            st.warning("👆 The number is lower than your guess.")
            st.session_state.attempts += 1

        # Store the user's guess in session state
        st.session_state.user_guess = user_guess

        display_attempts_left(st.session_state.attempts)

        # Check if the user has run out of attempts
        if st.session_state.attempts >= 5:
            st.error(f"🚨 You have run out of attempts. The number was {st.session_state.random_number}.")
            st.session_state.game_over = True

# Display the correct number if the game is over
if st.session_state.game_over:
    st.markdown("---")
    st.markdown(f"**The correct number was:** {st.session_state.random_number}")

#Next Turn
if st.button("Next Turn"):
    if not st.session_state.game_over:
        st.session_state.user_guess = 1  # Reset the user's guess
        st.rerun()

# Restart button
if st.button("Restart"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.user_guess = 1  # Reset the user's guess
    st.rerun()