# Minecraft-Music-Player
Play any music file using this noteblock-redstone device

Traditionally, making custom songs in Minecraft requires (very) long lines of noteblocks each manually adjusted for a specific song. This has a few problems:
1. Inconsistent audio: sound is dependent on where you are located relative to a note block, meaning you need to follow the lines of note blocks even to hear the song
2. No customization: you need to remake the entire system for every single new song
3. Not very scalable: the size of the Redstone system increases with the length of the piece, so doubling the song length means doubling the size

## What's different
1. Consistent audio: notes are played from 26 fixed note blocks
2. Very customizable: data is stored in binary format with shulker boxes, using shovels for 1s and any stackable blocks for 0s
3. Fixed size: the device runs any song regardless of length, which can theoretically run songs infinitely if given enough data
4. Survival friendly: song data is portable and reusable with shulker boxes, meaning a cheaper build for survival players

## How it works
Data is read from the shulker boxes in 5-bit lines, this data is then put through a 32-bit decoder which directs to the corresponding note block. When timed properly, the song is played according to specifications.
