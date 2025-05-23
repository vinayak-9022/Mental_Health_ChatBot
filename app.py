from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

def chatbot_response(user_input):
    """
    Generate a chatbot response based on the user's input.
    It detects moods like happy, sad, anxious, and provides motivational videos or breathing exercises.
    """
    # List of motivational video links
    motivational_videos = [
        "https://www.youtube.com/watch?v=4pFYpT_-7qk",  # "You Are Enough" motivational video
        "https://www.youtube.com/watch?v=wWW_KH_kEMI",  # TED Talk on overcoming depression
        "https://www.youtube.com/watch?v=hdJ5kJ3QGeY"   # How to Stay Positive in Tough Times
    ]
    
    # List of breathing exercises
    breathing_exercises = [
        "Try the 4-7-8 breathing technique:\n- Inhale for 4 seconds\n- Hold for 7 seconds\n- Exhale for 8 seconds",
        "Try Box Breathing:\n- Inhale for 4 seconds\n- Hold for 4 seconds\n- Exhale for 4 seconds\n- Hold again for 4 seconds",
        "Another option is the 5-5-5 technique:\n- Inhale for 5 seconds\n- Hold for 5 seconds\n- Exhale for 5 seconds"
    ]
    
    # Basic responses based on mood detection
    positive_responses = ["That's great to hear!", "Keep it up!", "I'm happy for you!"]
    negative_responses = [
        "I'm sorry you're feeling this way. It's okay to not feel okay. Here's something that might help:\n",
        "Try to take it slow and breathe. Things will get better. Here's a video you can watch:\n",
        "Take a break, Rest is important. Here's a motivational video:\n"
    ]
    neutral_responses = ["I'm here to chat if you need me!", "It's okay to feel neutral sometimes."]
    
    # Basic keyword matching for mood detection
    if "happy" in user_input.lower():
        return random.choice(positive_responses)
    elif "sad" in user_input.lower() or "depressed" in user_input.lower():
        # Suggest motivational video and breathing exercise
        video = random.choice(motivational_videos)
        exercise = random.choice(breathing_exercises)
        return f"{random.choice(negative_responses)}<a href='{video}' target='_blank'>Click here for a Motivational Video</a>\n\nAlso, try this breathing exercise to help calm down:\n{exercise}"
    elif "anxious" in user_input.lower() or "stressed" in user_input.lower():
        # Provide breathing exercise suggestion
        exercise = random.choice(breathing_exercises)
        return f"It sounds like you're feeling anxious. Try this breathing exercise to help:\n{exercise}"
    else:
        return random.choice(neutral_responses)

@app.route('/chat', methods=['POST'])
def chat():
    """
    This route receives a POST request with the user's input,
    processes it, and sends back a response.
    """
    # Get the user input from the request body
    user_input = request.json.get('user_input')
    print(f"Received user input: {user_input}")  # Log the input received by the backend

    # Generate the chatbot's response
    bot_response = chatbot_response(user_input)

    # Return the response as JSON
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)




