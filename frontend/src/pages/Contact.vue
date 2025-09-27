<template>
  <div class="min-h-screen bg-gray-900 text-white py-12 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12">
      <!-- Left Info Section -->
      <div class="space-y-6">
        <h1 class="text-4xl font-bold">Contact Us</h1>
        <p class="text-lg leading-relaxed">
          We are available for questions, feedback, or collaboration opportunities. Let us know how we can help!
        </p>
        <p class="text-lg leading-relaxed">
          You can also contact us at
          <a href="mailto:contact@quickblog.com" class="underline hover:text-orange-400">contact@quickblog.com</a>
          for any payment or course access related queries.
        </p>
      </div>

      <!-- Right Form Section -->
      <form class="bg-gray-800 p-8 rounded-lg shadow-lg space-y-6" @submit.prevent="submitForm">
        <div>
          <label for="name" class="block mb-2 font-semibold">Name</label>
          <input
            id="name"
            v-model="form.name"
            type="text"
            placeholder="Your Name"
            required
            class="w-full px-4 py-3 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
        </div>
        <div>
          <label for="email" class="block mb-2 font-semibold">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            placeholder="Email"
            required
            class="w-full px-4 py-3 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
        </div>
        <div>
          <label for="phone" class="block mb-2 font-semibold">Phone Number</label>
          <input
            id="phone"
            v-model="form.phone"
            type="tel"
            placeholder="Your 10-digit Number"
            class="w-full px-4 py-3 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
        </div>
        <div>
          <label for="subject" class="block mb-2 font-semibold">Subject</label>
          <input
            id="subject"
            v-model="form.subject"
            type="text"
            placeholder="Subject"
            class="w-full px-4 py-3 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
        </div>
        <div>
          <label for="message" class="block mb-2 font-semibold">Message</label>
          <textarea
            id="message"
            v-model="form.message"
            rows="5"
            placeholder="Type your message here."
            required
            class="w-full px-4 py-3 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-400 resize-none"
          ></textarea>
        </div>
        <div class="flex items-center space-x-3">
          <input
            id="recaptcha"
            type="checkbox"
            v-model="form.recaptcha"
            required
            class="w-5 h-5 rounded border-gray-600 bg-gray-700 focus:ring-2 focus:ring-orange-400"
          />
          <label for="recaptcha" class="select-none">I'm not a robot</label>
        </div>
        <button
          type="submit"
          class="w-full bg-orange-500 hover:bg-orange-600 transition-colors py-3 rounded font-semibold text-white shadow-lg"
        >
          Send Message
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContactPage",
  data() {
    return {
      form: {
        name: "",
        email: "",
        phone: "",
        subject: "",
        message: "",
        recaptcha: false,
      },
    };
  },
  methods: {
    submitForm() {
      alert(`Thank you, ${this.form.name}! Your message has been sent.`);
      this.form.name = "";
      this.form.email = "";
      this.form.phone = "";
      this.form.subject = "";
      this.form.message = "";
      this.form.recaptcha = false;
    },
  },
};
</script>

<style scoped>
/* Add any additional styling if needed */
</style>
