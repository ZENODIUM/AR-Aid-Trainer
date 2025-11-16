from flask import Flask, render_template, send_from_directory, request, jsonify
import mimetypes
import google.generativeai as genai

app = Flask(__name__)

GEMINI_API_KEY = ''
genai.configure(api_key=GEMINI_API_KEY)

mimetypes.add_type('model/gltf-binary', '.glb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    response = send_from_directory('static', filename)
    if filename.endswith('.glb'):
        response.headers['Content-Type'] = 'model/gltf-binary'
    return response

@app.route('/api/ai-assistant', methods=['POST'])
def ai_assistant():
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data received'}), 400
            
        action = data.get('action')  
        
        if not action:
            return jsonify({'success': False, 'error': 'No action specified'}), 400
        
      
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
        except Exception as e:
            try:
               
                model = genai.GenerativeModel('gemini-2.0-flash-exp')
            except Exception as e2:
                try:
                   
                    model = genai.GenerativeModel('gemini-1.5-flash')
                except Exception as e3:
                    return jsonify({'success': False, 'error': f'Model initialization failed: {str(e3)}'}), 500
        
        if action == 'init':
            # Initialize the gemini ai wwith full context for understanding
            procedure_name = data.get('procedure_name', 'Unknown')
            steps = data.get('steps', [])
            
            steps_text = '\n'.join([f"Step {s.get('number', '?')}: {s.get('text', '')} - Use {s.get('buttonText', '')}" for s in steps])
            
            prompt = f"""You are a helpful first aid training assistant for an AR simulation app. 

The app teaches users first aid procedures through interactive AR. Users see a 3D hand/leg with a wound and must apply the correct first aid items in the right order.

Current Procedure: {procedure_name}
Steps:
{steps_text}

Provide a very brief welcome message (1-2 sentences max, under 30 words) explaining what the user will learn. Keep it friendly and concise."""
            
        elif action == 'step_tips':
            # Tips for current step in the given procedure!
            procedure_name = data.get('procedure_name', 'Unknown')
            step_number = data.get('step_number', 1)
            step_text = data.get('step_text', '')
            tool_name = data.get('tool_name', 'tool')
            
            prompt = f"""You are a first aid training assistant.

Procedure: {procedure_name}
Current Step {step_number}: {step_text}
Tool to use: {tool_name}

Provide a very brief tip (1-2 sentences max, under 25 words) about this step. Be concise and practical."""
            
        elif action == 'error_hint':
            # hint the user when wrong object is used, so they can learn,
            procedure_name = data.get('procedure_name', 'Unknown')
            current_step = data.get('current_step', 1)
            step_text = data.get('step_text', '')
            correct_tool = data.get('correct_tool', 'correct tool')
            wrong_tool = data.get('wrong_tool', 'wrong tool')
            
            prompt = f"""You are a first aid training assistant.

The user is learning: {procedure_name}
Current Step {current_step}: {step_text}
User tried to use: {wrong_tool}
But should use: {correct_tool}

Give a friendly, helpful hint (1 sentence, under 20 words) guiding them to use the correct tool. Be encouraging and brief."""
            
        else:
            return jsonify({'success': False, 'error': 'Invalid action'}), 400
      
        try:
            response = model.generate_content(prompt)
            message = response.text if hasattr(response, 'text') else str(response)
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'API call failed: {str(e)}'
            }), 500
        
        return jsonify({
            'success': True,
            'message': message
        })
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"Error in ai_assistant: {error_trace}")
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': error_trace
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

