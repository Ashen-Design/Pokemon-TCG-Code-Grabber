# Pokémon TCG Code Grabber
This is a python-based OCR code grabber designed as a proof of concept and python practice.

*Demonstration:* [https://www.youtube.com/watch?v=d2ePaWR_dqc](https://www.youtube.com/watch?v=d2ePaWR_dqc) 
## Background
When buying a Pokémon TCG Booster pack, you also receive a code to redeem a pack of the same set for the online version of the game.

Many YouTubers show the code after opening the pack; this program was designed to show that you can capture the code on the back and have it automatically pasted to a clipboard to redeem online within seconds of seeing it on screen.

## Usage
1. Load an image/pause a video showing the code on the screen.
2. Use a screenshot program to take a screenshot and store it on your clipboard. (`Win+Shift+S` for Windows, `Command-Control-Shift-4` for Mac, Linux varies)
3. Run `pokemon.py` with the image in your clipboard.
4. It will upscale the image for better recognition.
5. The application will automatically detect the text and copy it to your clipboard.
6. A new window on the redemption page for Pokémon TCG Online will open ready to have the code pasted into the redemption section.
7. Paste the code and it should redeem successfully!

## Issues
Sometimes (depending on lighting/angle) the text is not correctly identified. Finding a point where the code is as straight as possible without anything covering it is best.
