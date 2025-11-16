# AR Aid Trainer
<img width="1280" height="720" alt="thumb" src="https://github.com/user-attachments/assets/e63f5f7a-eac8-4a6c-8749-ffacb395001f" />

An augmented reality first aid training application that teaches life-saving procedures through interactive 3D simulations and AI-powered guidance. Learn essential first aid skills using your device's camera, 3D models, and real-time AI assistance.

## Features

- **Augmented Reality Training**: Interactive 3D simulations using device camera and orientation sensors
- **AI-Powered Guidance**: Real-time tips and error hints using Gemini AI
- **Text-to-Speech**: Audio feedback for better learning experience
- **Multiple Procedures**: Three different first aid scenarios to practice
- **Visual Feedback**: Progress bars, color changes, and animations for realistic training
- **Mobile & Desktop Support**: Works on both mobile devices and desktop browsers

## Team

- vishnu - vs3164@nyu.edu

## Setup

1. Install Python 3.8 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure all 3D model files (.glb) are in the `static/` directory:
   - hand.glb
   - leg_foot.glb
   - cotton_ball.glb
   - basic_bottle.glb
   - bottle.glb
   - band_aid.glb
   - tweezers.glb
   - ice_cube.glb
   - cloth.glb
   - splint.glb
   - cellphone.glb
   - first_aid_kit.glb

4. Configure Gemini API key in `app.py` (if needed)

## Run

Start the Flask server:
```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000`

For mobile devices on the same network, use your computer's IP address instead of localhost.

### Used AI to Implement the AR and 3D Object Interactions

## Procedures

### 1. Cuts
Learn how to treat minor cuts and wounds:
1. **Apply cotton ball** - Hold for 7 seconds on the wound (cotton turns red to indicate pressure)
2. **Wash with water** - Hold water bottle for 5 seconds to clean the wound (wound color fades)
3. **Apply antiseptic** - Rub antiseptic for 3 seconds
4. **Apply bandaid** - Place bandaid on wound (sticks automatically)

### 2. Bee Sting
Practice removing a bee stinger safely:
1. **Remove stinger with tweezers** - Hold tweezers steady for 5 seconds (hand movement cancels progress)
2. **Wash with water** - Clean the area for 5 seconds
3. **Apply ice cube** - Place ice cube on the affected area
4. **Apply bandaid** - Cover with bandaid

### 3. Snakebite
Learn emergency snakebite treatment:
1. **Wrap cloth** - Wrap cloth around the wound area
2. **Place splint** - Immobilize the affected limb with a splint
3. **Call ambulance** - Use the phone to call for emergency help

## How to Interact

### Basic Controls

1. **Starting a Procedure**:
   - Select a procedure from the home screen
   - Allow camera access when prompted
   - Click "Place Hand" or "Place Leg" button to anchor the 3D model

2. **Selecting Tools**:
   - Click the first aid kit icon (bottom right) to open tool selection
   - Choose the required tool for the current step
   - The tool will appear at the bottom of the screen

3. **Using Tools**:
   - **Desktop**: Click and drag tools to move them
   - **Mobile**: Touch and drag tools on the screen
   - Place tools on the wound area to interact
   - Follow on-screen instructions and progress bars

4. **AI Assistant**:
   - Click the "AI Assistant" button (bottom left) to open chat
   - Receive real-time tips for each step
   - Get hints if you use the wrong tool
   - AI messages are spoken aloud automatically

5. **Completing Steps**:
   - Some steps require holding tools in place for a specific duration
   - Watch the progress bar to see remaining time
   - Visual feedback indicates successful completion
   - Move to the next step automatically upon completion

### Tips for Best Experience

- Use a well-lit environment for better camera tracking
- Hold your device steady, especially during tweezers step
- Follow the AI assistant guidance for optimal learning
- Complete steps in order for best results
- On mobile, use the back camera for better AR experience

## Technical Details

- **Frontend**: HTML5, JavaScript, Three.js for 3D rendering
- **Backend**: Flask (Python) web server
- **AI**: Google Gemini API for intelligent assistance
- **AR**: Device orientation API for spatial tracking
- **3D Models**: GLTF/GLB format models
- **TTS**: Web Speech API for text-to-speech

## Future Scope

### Planned Features

- **Additional Procedures**: 
  - CPR training with chest compression feedback
  - Choking (Heimlich maneuver)
  - Burns treatment
  - Fracture immobilization
  - Allergic reactions (EpiPen usage)

- **Enhanced Interactions**:
  - Haptic feedback for realistic touch sensations
  - Multiplayer training sessions
  - Performance scoring and analytics
  - Certification system upon completion

- **Advanced AI Features**:
  - Real-time pose detection for procedure validation
  - Personalized learning paths
  - Adaptive difficulty based on user performance
  - Voice commands for hands-free operation

- **Improved AR**:
  - Markerless AR using WebXR
  - Better hand/body tracking
  - Realistic physics simulation
  - Environmental awareness

- **Educational Enhancements**:
  - Video tutorials integration
  - Quiz mode for knowledge testing
  - Progress tracking and history
  - Social sharing of achievements

- **Accessibility**:
  - Multiple language support
  - Voice-only mode for visually impaired
  - Simplified UI for beginners
  - Offline mode capability
    
## Resources

- **AI Model**: Google Gemini 2.5 Flash for intelligent assistance and guidance
- **3D Assets**: Sketchfab (https://sketchfab.com) for 3D models and assets
- **AR Framework**: Three.js (https://threejs.org) for 3D rendering and AR simulation
  
## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
