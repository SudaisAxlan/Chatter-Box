from flask import Flask,request,jsonify
def sendMessage():
    
   if request.method == "POST":
        data = request.get_json()  # Get the JSON payload from the request
        
        # Extract fields from the payload
        sender_id = data.get("sender_id")
        receiver_id = data.get("receiver_id")
        message = data.get("message")
        
        # Validate input
        if not sender_id or not receiver_id or not message:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Process the message (for now, just return it as a response)
        response_data = {
            "status": "Message sent successfully!",
            "data": {
                "sender_id": sender_id,
                "receiver_id": receiver_id,
                "message": message,
            }
        }
        
        return jsonify(response_data), 200
        
    