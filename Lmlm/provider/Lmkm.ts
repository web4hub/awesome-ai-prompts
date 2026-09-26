const prompt = await AuraPrompt.load("ui/luxury-watch");

await prompt.execute({
  provider: "lmlm",
  variables: {
      product_name: "Aura Watch",
      theme: "Glassmorphism"
  }
});
