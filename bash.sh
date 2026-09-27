git clone https://github.com/web4hub/prompts.chat.git
cd prompts.chat
npm install && npm run setup
kubu prompt search shader
kubu prompt execute luxury-watch
kubu prompt translate luxury-watch --lang fr
kubu prompt lint prompts/
kubu prompt embed prompts/
kubu prompt publish
curl -fsSL https://raw.githubusercontent.com/OpenArt-AI/cli/main/install.sh | sh
irm https://raw.githubusercontent.com/OpenArt-AI/cli/main/install.ps1 | iex
$openart login
openart generate image "a red fox in the snow" --model nano-banana-2 -o ./out/
