from pydub import AudioSegment


for i in range(1,11):


    input_file = f"{i}.m4a"  
    output_file = f"{i}.wav"  

    try:
        sound = AudioSegment.from_file(input_file)
        sound.export(output_file, format="wav")
        print("Conversion successful!")
    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")