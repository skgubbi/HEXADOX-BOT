export default {
  async fetch(request, env) {

    if (request.method !== "POST") {
      return new Response("HEXADOX BOT RUNNING");
    }

    const update = await request.json();

    if (update.message) {
      const chatId = update.message.chat.id;
      const text = update.message.text;

      if (text === "/start") {
        await sendMessage(
          env.BOT_TOKEN,
          chatId,
          "Welcome to Hexadox Pharmaceuticals Dermatology Catalogue.\n\nType /catalogue to view products."
        );
      }

      if (text === "/catalogue") {
        await sendMessage(
          env.BOT_TOKEN,
          chatId,
          "Hexadox Product Catalogue\n\n1. Trichology Range\n2. Anti-Fungal Range\n3. Anti-Acne Range\n4. Cosmetology Range"
        );
      }
    }

    return new Response("OK");
  }
};


async function sendMessage(token, chatId, message) {

  const url = `https://api.telegram.org/bot${token}/sendMessage`;

  await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      chat_id: chatId,
      text: message
    })
  });

}
