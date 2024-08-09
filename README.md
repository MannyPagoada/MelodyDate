# MelodyDate
---
## Summary

MelodyDate is a Python-based application that generates a unique ballad based on a user's birthday. By leveraging music theory and machine learning, the program transforms each birthday into a personalized musical experience. Each month is mapped to a specific key, while the day of the month determines the rhythm subdivision, selecting from a range of common patterns. The digits of the year influence the tones played by four different instruments, creating a distinctive melody that reflects the user's birthdate.

The application features a simple and intuitive GUI, allowing users to input their birthday and instantly generate a song. To ensure each date produces a unique composition, a machine learning model trained with PyTorch introduces subtle variations in melody, harmony, and rhythm. This model draws from a dataset of musical patterns, ensuring that no two songs are exactly alike.

Once the musical parameters are determined, the program uses MIDI files to create and playback the song. The resulting one-minute ballad can be saved as a MIDI or audio file, offering users a keepsake of their personalized melody. MelodyDate combines the precision of algorithmic composition with the creativity of machine learning, resulting in an innovative tool that transforms a simple date into a harmonious and memorable experience.