# MelodyDate

**MelodyDate** is a Python-based application that generates a unique ballad based on a user's birthday. By leveraging music theory and machine learning, the program transforms each birthday into a personalized musical experience. Each month is mapped to a specific key, while the day of the month determines the rhythm subdivision, selecting from a range of common patterns. The digits of the year influence the tones played by four different instruments, creating a distinctive melody that reflects the user's birthdate.

The application features a simple and intuitive GUI, allowing users to input their birthday and instantly generate a song. To ensure each date produces a unique composition, a machine learning model trained with PyTorch introduces subtle variations in melody, harmony, and rhythm. This model draws from a dataset of musical patterns, ensuring that no two songs are exactly alike.

Once the musical parameters are determined, the program uses MIDI files to create and playback the song. The resulting one-minute ballad can be saved as a MIDI or audio file, offering users a keepsake of their personalized melody. MelodyDate combines the precision of algorithmic composition with the creativity of machine learning, resulting in an innovative tool that transforms a simple date into a harmonious and memorable experience.

---
## Tools Used

- **Python**: Primary programming language for development.
- **PyTorch**: For machine learning model training and implementation.
- **midiutil**: For creating and manipulating MIDI files.
- **pydub**: For audio processing and conversion.
- **Tkinter**: For building the GUI.
- **librosa**: For audio and music analysis.
- **numpy**: For numerical computations.
- **pretty_midi**: Optional library for working with MIDI files.

---
## System Design

1. **User Interface (UI)**:
   - A simple GUI to collect the user's birthday input.
   - This UI will interact with the backend to generate the song.

2. **Backend Logic**:
   - **Birthday Processing**: Convert the birthday into musical parameters (key, subdivision, tones).
   - **Song Structure**: Define the structure of the ballad (e.g., intro, verse, chorus).
   - **Music Generation**: Use the musical parameters to generate a unique melody, harmony, and rhythm.
   - **Machine Learning Model**: Generate unique variations using a trained model.

3. **Audio Generation**:
   - Convert the generated musical data (MIDI) into audio.
   - Use predefined instrument sounds or synthesized sounds.

4. **Output**:
   - Play the generated song.
   - Optionally, export the song to a file (e.g., WAV or MIDI).

# MelodyDate Development Plan

---
## Overview
This plan outlines the steps required to develop **MelodyDate**, a Python-based application that generates a unique ballad based on a user's birthday. The project is expected to be completed in approximately one month.

## Week 1: Setup and Initial Development

### Day 1-2: Environment Setup
- Install Python and set up a virtual environment.
- Install necessary libraries: `pytorch`, `midiutil`, `pydub`, `Tkinter`, `librosa`, `numpy`, and `pretty_midi`.

### Day 3-4: Create Project Structure
- Organize the project into folders: `ui`, `music_generation`, `ml_model`, `output`.
- Set up version control with Git.

### Day 5-7: Implement Basic GUI
- Develop a simple user interface using `Tkinter` for inputting the birthday.
- Add basic functionality for capturing user input.

## Week 2: Core Functionality Development

### Day 8-10: Develop Birthday Processing Module
- Implement logic to convert birthday into musical parameters (key, subdivision, tones).
- Test and verify the processing of different birthdays.

### Day 11-13: Define Song Structure
- Create a basic structure for the ballad (e.g., intro, verse, chorus).
- Develop initial logic for generating melody, harmony, and rhythm based on parameters.

### Day 14: Integrate Basic Music Generation
- Use `midiutil` or `pretty_midi` to create MIDI files from generated parameters.
- Ensure basic functionality of music generation and playback.

## Week 3: Machine Learning Integration

### Day 15-17: Data Collection and Preparation
- Gather a dataset of melodies or rhythm patterns.
- Extract features using `librosa` or similar libraries.

### Day 18-20: Model Training
- Train a machine learning model using PyTorch to generate musical variations.
- Test the model with sample data and adjust as needed.

### Day 21-22: Integrate ML Model
- Integrate the trained model into the music generation logic.
- Ensure the model influences melody, harmony, and rhythm as intended.

## Week 4: Finalization and Testing

### Day 23-25: Complete Audio Generation
- Convert MIDI files to audio using `pydub` or other libraries.
- Implement audio playback and file export functionality.

### Day 26-27: Testing and Debugging
- Test the complete system with various birthdays to ensure correct functionality.
- Debug and refine the application based on test results.

### Day 28-29: Final Touches
- Improve the UI based on feedback.
- Add documentation and usage instructions.

### Day 30: Project Wrap-Up
- Review and finalize code.
- Prepare and upload the project to a repository.
- Write and include the README.md file.


---
## Conclusion
By following this plan, **MelodyDate** will be developed and ready for use within one month, offering a unique and personalized musical experience based on user birthdays.


MelodyDate/
│
├── ui/
│   ├── __init__.py
│   ├── main.py        # Main GUI application script
│   ├── ui_helpers.py  # Helper functions for the UI
│   └── assets/        # Any assets like images or icons
│
├── music_generation/
│   ├── __init__.py
│   ├── melody.py      # Functions to generate the melody based on birthday
│   ├── harmony.py     # Functions for harmony and rhythm generation
│   ├── midi_utils.py  # MIDI file creation and manipulation
│   └── music_theory.py  # Music theory related functions and constants
│
├── ml_model/
│   ├── __init__.py
│   ├── model.py       # Definition of the machine learning model
│   ├── training.py    # Training script for the machine learning model
│   ├── inference.py   # Script for using the model to generate variations
│   └── data/          # Directory for storing datasets or pre-trained models
│
└── output/
    ├── __init__.py
    ├── save_midi.py   # Script for saving the generated music as MIDI or audio files
    └── saved_files/  # Directory to store saved MIDI or audio files