import os
import imageio
from PIL import Image, ImageDraw, ImageFont
from pygments import highlight, lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token
import time
 
# Configuration
code = '''
package com.user.define.exception.handling;

import  java.util.Scanner;

public class AgeException extends Exception {

    AgeException(String message){
        super(message);
    }

    public  static void main(String[] args){

        Scanner scan = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = scan.nextInt();

        try{
            checkAge(age);
        } catch (Exception e) {
            System.out.println("A problem occured: "+e);
        }

    }

    static void checkAge(int age)throws AgeException{
        if(age < 18 ){
            throw new AgeException("\n"+"you must be 18+ sign up");
        }
        else{
            System.out.println("You are now signed up!");
        }
    }

}



'''  # Replace with your code
output_file = 'code.gif'
font_size = 14
font_color = (255, 255, 255)  # RGB color for text (white in this case)
code_background_color = (34, 39, 46)  # RGB color for code background
container_background_color = (34, 39, 46)  # RGB color for container background
padding = 10
frame_duration = 0.1  # Duration of each frame in seconds
char_duration = 0.01  # Duration between each character in seconds

# Calculate dimensions
font = ImageFont.truetype('verdana', font_size)  # Replace with your font file
line_height = font.getsize('hg')[1]
lines = code.split('\n')
num_lines = len(lines)
line_widths = [font.getsize(line)[0] for line in lines]
max_line_width = max(line_widths)
image_width = max_line_width + 2 * padding
image_height = (line_height * num_lines) + 2 * padding

# Create frames
frames = []
lexer = get_lexer_by_name('python', stripall=True)
tokens = list(lex(code, lexer))

for line_num, line in enumerate(lines):
    image = Image.new('RGB', (image_width, image_height), container_background_color)
    draw = ImageDraw.Draw(image)

    # Draw previously written lines
    for prev_line_num in range(line_num):
        prev_line = lines[prev_line_num]
        prev_tokens = list(lex(prev_line, lexer))
        x, y = padding, padding + (line_height * prev_line_num)
        for token in prev_tokens:
            token_text = token[1]
            if token[0] in Token.Keyword:
                draw.text((x, y), token_text, font=font, fill=(35, 169, 242))  # Blue color for keywords
            elif token[0] in Token.Literal.Number:
                draw.text((x, y), token_text, font=font, fill=(252, 252, 84))  # Yellow color for numbers
            else:
                draw.text((x, y), token_text, font=font, fill=font_color)
            x += font.getsize(token_text)[0]

    # Draw current line
    x, y = padding, padding + (line_height * line_num)
    tokens = list(lex(line, lexer))
    for token in tokens:
        token_text = token[1]
        if token[0] in Token.Keyword:
            for char in token_text:
                draw.text((x, y), char, font=font, fill=(35, 169, 242))  # Blue color for keywords
                x += font.getsize(char)[0]
                frames.append(image.copy())
                time.sleep(char_duration)
        elif token[0] in Token.Literal.Number:
            for char in token_text:
                draw.text((x, y), char, font=font, fill=(252, 252, 84))  # Yellow color for numbers
                x += font.getsize(char)[0]
                frames.append(image.copy())
                time.sleep(char_duration)
        else:
            for char in token_text:
                draw.text((x, y), char, font=font, fill=font_color)
                x += font.getsize(char)[0]
                frames.append(image.copy())
                time.sleep(char_duration)

# Generate output filename
base_filename = os.path.splitext(output_file)[0]
extension = os.path.splitext(output_file)[1]
output_filename = output_file
index = 1
while os.path.isfile(output_filename):
    output_filename = f"{base_filename}({index}){extension}"
    index += 1

# Save frames as GIF
imageio.mimsave(output_filename, frames, duration=frame_duration)
