
import re
import json
import os 
import sys
def parse_messages_to_json(input_text, output_file=None):
    """
    Parses the given text of messages and returns a JSON string
    conforming to the schema:
    
    {
      "id": <integer>,
      "message": <string>,
      "reply to": <integer or None>,
      "userId": <string>,
      "datetime": <string>
    }
    
    Parameters:
    -----------
    input_text : str
        The raw text containing messages in the specified format.
    output_file : str, optional
        If provided, the resulting JSON array is also written to this file.
    
    Returns:
    --------
    str
        A JSON-formatted string containing a list of message objects.
    """
    # Split the input by double newlines to separate message blocks
    blocks = input_text.strip().split("\n\n")
    
    messages = []
    
    for block in blocks:
        lines = block.strip().split("\n")
        
        # First line matches: message-<id>: <userId> <YYYY-MM-DD HH:MM:SS>
        # Example: "message-66310: user154747748 2020-08-17 23:58:46"
        header_pattern = r"^message-(\d+):\s+(user\d+)\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})"
        header_match = re.match(header_pattern, lines[0])
        if not header_match:
            # If the format is broken, skip this block or handle error
            continue
        
        message_id = int(header_match.group(1))
        user_id = header_match.group(2)
        datetime_str = header_match.group(3)
        
        # Initialize reply_to as None
        reply_to_id = None
        
        # Determine if the second line is a "Reply to:" line or message text
        # The line would match: "Reply to: message-<id>"
        reply_pattern = r"^Reply to:\s+message-(\d+)$"
        
        # We need to see if there's at least a second line
        # and if it matches the "Reply to" pattern.
        message_text_start_index = 1
        if len(lines) > 1:
            reply_match = re.match(reply_pattern, lines[1])
            if reply_match:
                # Found a reply-to line
                reply_to_id = int(reply_match.group(1))
                message_text_start_index = 2
        
        # The rest of the lines (from message_text_start_index onward) form the message body
        message_lines = lines[message_text_start_index:]
        message_text = "\n".join(message_lines).strip()
        
        # Build the dictionary for this message
        msg_dict = {
            "id": message_id,
            "message": message_text,
            "replyTo": reply_to_id,
            "userId": user_id,
            "datetime": datetime_str
        }
        
        messages.append(msg_dict)
    
    # Convert the list of messages to JSON
    json_result = json.dumps(messages, indent=4, ensure_ascii=False)
    
    # If an output file is specified, write to it
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(json_result)
    
    # Also return the JSON string
    return json_result

def add_id_labels_to_json(json_file_path: str):
    labaled_json_file_path = json_file_path.replace(".json", "_labeled.json")
    json_data = None
    labaled_json_data = {}
    try : 
        with open(json_file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        for i, msg in enumerate(json_data):
            labaled_json_data[f"message_{msg['id']}"] = msg
        with open(labaled_json_file_path, "w", encoding="utf-8") as f:
            json.dump(labaled_json_data, f, indent=4, ensure_ascii=False)
    except : 
        print(f"Error reading file {json_file_path}")
    return 
    
def convert_txt_to_str(file_path : str) -> str:
    if  file_path.endswith("txt"):
        with open(file_path, "r",encoding="utf-8") as file:
            return str(file.read())
    else : 
        raise ValueError("The file must be a .txt file.") 
if __name__ == "__main__":
    # base_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path="resources/messages_1001_en.txt"
    input_file_path = os.path.join(base_path, file_path.split("/")[0])
    input_file_path = os.path.join(input_file_path, file_path.split("/")[1])
    print(f"Processing {input_file_path}")
    raw_input = convert_txt_to_str(input_file_path)
    json_output = parse_messages_to_json(raw_input)
    with open("messages_json.json", "w", encoding="utf-8") as f:
        f.write(json_output)
    add_id_labels_to_json("messages_json.json")
    print(json_output)
