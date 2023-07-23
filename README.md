# Voice-Assistant-Python

## Voice Assistant with Speech Recognition

This is a simple Python-based Voice Assistant program that uses speech recognition, text-to-speech conversion, and web browser integration to perform various tasks based on voice commands.

## How it Works

The Voice Assistant interacts with the user by listening to their voice commands, processing the queries, and responding appropriately. It has the following main components:

1. Speech Recognition: The program uses the speech_recognition library to capture the user's voice input.

2. Text-to-Speech Conversion: The pyttsx3 library is utilized to convert the Assistant's responses into speech.

3. Web Browsing: The Assistant can open specific websites like Google, YouTube, LinkedIn, GitHub, and HackerRank based on the user's commands.

## Prerequisites

Make sure you have the necessary libraries installed. You can install them using pip:

pip install speech_recognition pyttsx3

## Usage

1. Run the Python script Voice Assistant.py.

2. The Assistant will greet you and wait for your voice command.

3. Speak your command after the prompt "Listening...".

4. The Assistant will process the command and respond accordingly.

## Supported Commands

The Voice Assistant currently supports the following commands:

1. "Hello": The Assistant will greet you and ask how it can assist you.

2. "Goodbye": The Assistant will bid farewell and end the program.

3. "Quit" or "Exit": The Assistant will confirm and terminate the program.

4. "Open Google": The Assistant will open the Google homepage in your default web browser.

5. "Open YouTube": The Assistant will open a specific YouTube channel in your default web browser.

6. "Open LinkedIn": The Assistant will open a specific LinkedIn profile in your default web browser.

7. "Open Code": The Assistant will open a specific GitHub profile in your default web browser.

8. "Open HackerRank": The Assistant will open a specific HackerRank profile in your default web browser.

Customization

You can extend the functionality of the Voice Assistant by adding more commands or integrating it with other APIs and services.
