"""
Seed script: creates sample blogs with generated placeholder images for all categories.
Run after `python setup.py` has created the database.
"""

import os
import random
from datetime import datetime, timedelta
from app import create_app
from models import db, Blog, User, Category

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

CATEGORY_COLORS = {
    "Tech": ("#2563eb", "#1d4ed8"),       # blue
    "AI": ("#7c3aed", "#6d28d9"),         # purple
    "Lifestyle": ("#059669", "#047857"),  # emerald
    "Finance": ("#d97706", "#b45309"),    # amber
    "Design": ("#ec4899", "#db2777"),     # pink
    "Science": ("#0891b2", "#0e7490"),    # cyan
}

BLOG_DATA = {
    "Tech": [
        {
            "title": "The Rise of WebAssembly: What It Means for Modern Web Development",
            "subtitle": "How WASM is changing the landscape of browser-based applications",
            "description": "📌 Introduction\nWebAssembly (WASM) is transforming how we build for the web. This low-level binary format allows languages like C, C++, and Rust to run in the browser at near-native speed.\n\n⚡ Performance Breakthrough\nUnlike JavaScript, WASM is compiled ahead of time into a binary format that browsers can execute without parsing. This means complex applications like video editors, 3D games, and scientific simulations can now run smoothly in the browser.\n\n🔧 Developer Experience\nMajor frameworks are already embracing WASM. Blazor lets C# developers build full-stack web apps, while Rust's WebAssembly ecosystem is growing rapidly with tools like Yew and Seed.\n\n🌐 Real-World Applications\nCompanies like Figma, Google Earth, and AutoCAD have already adopted WASM for performance-critical features. The potential extends to serverless computing, edge functions, and IoT.\n\n🎯 Conclusion\nWebAssembly isn't replacing JavaScript — it's complementing it. Frontend developers should start experimenting with WASM to stay ahead of the curve.",
        },
        {
            "title": "Understanding Edge Computing: The Next Frontier in Cloud Architecture",
            "subtitle": "Why processing data closer to the source is the future of infrastructure",
            "description": "📌 Introduction\nEdge computing moves computation and data storage closer to where data is generated. Instead of sending everything to centralized cloud servers, processing happens at the edge — right where the IoT sensors, cameras, and devices live.\n\n🚀 Speed and Latency\nFor applications like autonomous vehicles or real-time manufacturing, every millisecond counts. Edge computing reduces latency dramatically by eliminating the round trip to distant data centers.\n\n💰 Cost Efficiency\nProcessing data at the edge means less bandwidth usage and lower cloud costs. Only relevant, aggregated data needs to be sent to the cloud for long-term storage or analysis.\n\n🔒 Security Benefits\nKeeping sensitive data at the edge reduces exposure to cloud-based vulnerabilities. Healthcare and finance industries are adopting edge architectures to meet compliance requirements.\n\n🎯 Conclusion\nEdge computing is not replacing the cloud — it's extending it. As 5G rolls out globally, edge computing will become the standard architecture for real-time applications.",
        },
    ],
    "AI": [
        {
            "title": "Large Language Models: How GPT and Its Successors Are Reshaping Industries",
            "subtitle": "From customer service to code generation, LLMs are everywhere",
            "description": "📌 Introduction\nLarge Language Models (LLMs) like GPT-4, Claude, and Gemini have moved beyond novelty into production. Businesses across every sector are finding ways to leverage these powerful tools.\n\n💼 Enterprise Adoption\nCustomer support chatbots, automated report generation, and document summarization are just the beginning. Companies are saving millions by automating repetitive knowledge work.\n\n🛠️ Developer Tools\nGitHub Copilot, Amazon CodeWhisperer, and similar tools are making developers more productive. Code completion, bug detection, and automated testing are being transformed by AI assistance.\n\n⚖️ Challenges and Ethics\nHallucinations, bias, and data privacy remain significant challenges. Responsible AI practices, human oversight, and transparent model cards are essential for safe deployment.\n\n🎯 Conclusion\nLLMs are a paradigm shift, not just a trend. Organizations that learn to integrate AI thoughtfully will have a significant competitive advantage in the coming years.",
        },
        {
            "title": "Computer Vision Breakthroughs: From Medical Imaging to Autonomous Vehicles",
            "subtitle": "How machines are learning to see and understand the visual world",
            "description": "📌 Introduction\nComputer vision has made remarkable progress. Models can now detect tumors in medical scans with greater accuracy than human radiologists, and self-driving cars navigate complex urban environments.\n\n🏥 Healthcare Revolution\nAI-powered imaging is detecting cancers, fractures, and rare diseases earlier than ever before. Pathologists use vision models to analyze biopsy slides, reducing diagnostic time by 60%.\n\n🚗 Autonomous Driving\nTesla, Waymo, and Cruise are pushing the boundaries of what cameras and neural networks can achieve. Object detection, lane tracking, and pedestrian prediction have improved dramatically.\n\n🛒 Retail and Manufacturing\nVisual inspection systems catch defects in real-time on production lines. Cashier-less stores use hundreds of cameras to track what customers pick up.\n\n🎯 Conclusion\nComputer vision is moving from research labs into every industry. The next wave will bring even more accurate models that require less training data.",
        },
    ],
    "Lifestyle": [
        {
            "title": "The Science of Morning Routines: What High Performers Do Before 8 AM",
            "subtitle": "Simple habits that set the tone for a productive day",
            "description": "📌 Introduction\nThe way you start your morning determines the trajectory of your entire day. High performers across every field share common habits that prime them for peak performance.\n\n☀️ Hydration and Movement\nDrinking water immediately after waking rehydrates your brain and body. Follow with 10 minutes of stretching or light exercise to increase blood flow and mental clarity.\n\n🧘 Mindfulness and Planning\nFive minutes of meditation reduces anxiety and improves focus. Then write down your top three priorities for the day — not a long list, just what matters most.\n\n📚 Learning First\nReading for 20 minutes before checking email or social media fills your mind with quality input first. Your brain is most receptive to new information in the morning.\n\n🥗 Nutrition Matters\nA protein-rich breakfast stabilizes blood sugar and sustains energy. Skip the sugar spikes that lead to mid-morning crashes.\n\n🎯 Conclusion\nYou don't need a complicated routine. Consistency with a few key habits — hydration, movement, mindfulness, and learning — compounds into extraordinary results over time.",
        },
        {
            "title": "Digital Minimalism: Reclaiming Focus in an Age of Distraction",
            "subtitle": "How to use technology intentionally without letting it use you",
            "description": "📌 Introduction\nWe spend an average of 6 hours per day on digital devices. Digital minimalism isn't about quitting technology — it's about using it with intention and purpose.\n\n📱 The Cost of Constant Notifications\nEach notification fragments your attention. Researchers estimate it takes 23 minutes to fully refocus after a distraction. Turn off all non-essential notifications today.\n\n🗑️ The Great App Purge\nAudit every app on your phone. Ask: Does this add genuine value to my life? Delete or hide everything else. Most people cut 60% of their apps without missing them.\n\n⏰ Scheduled Batching\nCheck email and social media at set times — twice per day maximum. Batch all communication into focused 20-minute blocks instead of constant context-switching.\n\n🌿 Boredom Is Essential\nAllow yourself to be bored. Don't reach for your phone in every waiting moment. Some of the best ideas emerge when your mind is allowed to wander.\n\n🎯 Conclusion\nDigital minimalism creates space for deep work, meaningful relationships, and genuine creativity. Start with one change today and build from there.",
        },
    ],
    "Finance": [
        {
            "title": "Compound Interest: The Eighth Wonder of the World Explained",
            "subtitle": "How small investments today can grow into life-changing wealth",
            "description": "📌 Introduction\nAlbert Einstein reportedly called compound interest the eighth wonder of the world. Those who understand it earn it; those who don't, pay it. Here's how to make it work for you.\n\n📐 The Math Made Simple\nCompound interest means earning interest on your interest. If you invest $1,000 with a 10% annual return, you get $1,100 in year one. In year two, you earn 10% on $1,100, giving you $1,210. Over decades, this exponential growth is staggering.\n\n⏰ Time Is Your Greatest Asset\nStarting early is more important than investing large amounts. A person who invests $200/month from age 25 to 35 ends up with more at 65 than someone who invests $200/month from 35 to 65.\n\n📊 Index Funds and ETFs\nLow-cost index funds that track the S&P 500 have historically returned ~10% annually. They require no stock-picking skill and minimize fees that eat into compounding.\n\n🚫 The Debt Trap\nCompound interest works against you with credit card debt. At 22% APR, a $5,000 balance can double in just over three years. Pay off high-interest debt before investing.\n\n🎯 Conclusion\nStart today, even with small amounts. Be consistent. Let time and compounding do the heavy lifting. Your future self will thank you.",
        },
        {
            "title": "Building Multiple Income Streams: A Practical Guide for 2025",
            "subtitle": "Why the wealthiest people never rely on a single source of income",
            "description": "📌 Introduction\nRelying on a single paycheck is risky. The pandemic taught us that jobs can disappear overnight. Building multiple income streams isn't greed — it's resilience.\n\n💼 Active vs. Passive Income\nActive income trades time for money (your day job). Passive income, once set up, generates money with minimal ongoing effort: digital products, affiliate marketing, rental properties, dividend stocks.\n\n🏗️ Start a Side Business\nYour skills are valuable. Consulting, freelancing, or creating an online course can generate significant side income. Start small — one client, one product — and scale.\n\n📈 Invest in Dividend Stocks\nDividend-paying stocks provide regular cash payments. Reinvest those dividends to buy more shares, accelerating your compounding machine.\n\n🏡 Real Estate and REITs\nRental properties provide monthly income plus appreciation. Real Estate Investment Trusts (REITs) let you invest in property without being a landlord.\n\n🎯 Conclusion\nAim for three to five income streams. Each one adds stability and accelerates your path to financial freedom. Start with one, make it work, then add another.",
        },
    ],
    "Design": [
        {
            "title": "Design Systems in 2025: Building Consistent, Scalable User Interfaces",
            "subtitle": "How component-driven design saves time and creates better products",
            "description": "📌 Introduction\nA design system is a collection of reusable components, patterns, and guidelines that ensure visual and functional consistency across a product. Every major company has one.\n\n🧩 Components vs. Patterns\nComponents are the building blocks: buttons, inputs, cards, modals. Patterns are solutions to common problems: authentication flows, search experiences, onboarding sequences.\n\n🎨 Design Tokens\nTokens are the atoms of your system — colors, typography, spacing, shadows. Define them once and reference everywhere. This makes global updates trivial.\n\n📚 Documentation Is Key\nA design system without documentation is just a component library. Document usage guidelines, accessibility requirements, and code examples for every component.\n\n🔄 Versioning and Governance\nTreat your design system like a product. Version it, communicate changes, and have a governance process for additions and modifications.\n\n🎯 Conclusion\nDesign systems pay for themselves many times over by reducing design debt, speeding up development, and creating a cohesive user experience.",
        },
        {
            "title": "The Psychology of Color in UI Design: How to Choose the Right Palette",
            "subtitle": "Understanding how colors affect user behavior and perception",
            "description": "📌 Introduction\nColor is one of the most powerful tools in a designer's arsenal. It influences emotion, guides attention, and can dramatically affect conversion rates.\n\n❤️ Red: Urgency and Passion\nRed increases heart rate and creates a sense of urgency. It's why clearance sales use red tags and why many CTA buttons are red or orange.\n\n💙 Blue: Trust and Professionalism\nBlue is the most used color in corporate design for a reason. It conveys stability, trust, and professionalism. Financial institutions and healthcare apps lean heavily on blue.\n\n💚 Green: Growth and Harmony\nGreen represents nature, health, and financial growth. It works well for wellness apps, environmental brands, and anything related to money.\n\n🟡 Yellow: Optimism and Caution\nYellow grabs attention quickly. Use it sparingly for highlights and warnings. Too much yellow can cause eye strain.\n\n🎯 Conclusion\nChoose a primary color that aligns with your brand values, a secondary for contrast, and neutral tones for the majority of your interface. Test with real users before committing.",
        },
    ],
    "Science": [
        {
            "title": "Quantum Computing Explained: Why It Matters Beyond the Hype",
            "subtitle": "The real-world applications that make quantum computing revolutionary",
            "description": "📌 Introduction\nQuantum computing isn't just faster computing — it's a fundamentally different way of processing information. Instead of bits (0 or 1), quantum computers use qubits that can exist in multiple states simultaneously.\n\n🔬 How Qubits Work\nThrough superposition and entanglement, qubits explore many possible solutions at once. A quantum computer with 300 qubits could process more possibilities than there are atoms in the observable universe.\n\n💊 Drug Discovery\nSimulating molecular interactions is extremely hard for classical computers. Quantum computers can model complex molecules accurately, potentially cutting drug discovery timelines from years to months.\n\n🌍 Climate Modeling\nQuantum computers could create detailed climate models that account for countless variables simultaneously, helping us understand and mitigate climate change.\n\n🔐 Cryptography Impact\nQuantum computers will break current encryption methods. Post-quantum cryptography is already being standardized to prepare for this eventuality.\n\n🎯 Conclusion\nQuantum computing is still in its early stages, but its potential is immense. We are in the quantum decade — the foundational breakthroughs are happening now.",
        },
        {
            "title": "CRISPR and Gene Editing: The Promise and Perils of Rewriting DNA",
            "subtitle": "How scientists are curing diseases by editing the code of life",
            "description": "📌 Introduction\nCRISPR-Cas9 is a gene-editing tool that allows scientists to modify DNA with unprecedented precision. It's already being used in clinical trials to treat sickle cell disease and certain cancers.\n\n🧬 How CRISPR Works\nCRISPR uses a guide RNA to find a specific DNA sequence, then the Cas9 protein cuts the DNA at that exact location. The cell's natural repair mechanisms then make the edit.\n\n💉 Medical Breakthroughs\nThe first CRISPR-based therapy was approved in 2023 for sickle cell disease. Trials for inherited blindness, muscular dystrophy, and HIV are underway.\n\n🌾 Agricultural Applications\nGene-edited crops can be more nutritious, drought-resistant, and require fewer pesticides. Unlike GMOs, CRISPR edits can be indistinguishable from natural mutations.\n\n⚖️ Ethical Considerations\nEditing human embryos is controversial. Germline edits would be passed to future generations. The scientific community is debating where to draw the line.\n\n🎯 Conclusion\nCRISPR is one of the most transformative technologies of our time. Used responsibly, it could eliminate thousands of genetic diseases and help feed a growing planet.",
        },
    ],
}


def generate_placeholder_image(category_name, title, index):
    """Generate a simple placeholder image with category color and title."""
    from PIL import Image, ImageDraw, ImageFont

    width, height = 800, 500
    color1, color2 = CATEGORY_COLORS.get(category_name, ("#6b7280", "#4b5563"))

    img = Image.new("RGB", (width, height), color1)
    draw = ImageDraw.Draw(img)

    for i in range(0, height, 4):
        alpha = int(255 * (0.3 + 0.3 * (i / height)))
        overlay = Image.new("RGBA", (width, 4), (*hex_to_rgb(color2), alpha))
        img.paste(overlay, (0, i), overlay)

    try:
        font_large = ImageFont.truetype("arialbd.ttf", 48)
        font_small = ImageFont.truetype("arial.ttf", 28)
    except Exception:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    _, _, w, _ = draw.textbbox((0, 0), category_name, font=font_large)
    draw.text(((width - w) / 2, 140), category_name, fill="white", font=font_large)

    lines = []
    line = ""
    for word in title.split():
        test = line + " " + word if line else word
        _, _, tw, _ = draw.textbbox((0, 0), test, font=font_small)
        if tw > width - 80:
            lines.append(line)
            line = word
        else:
            line = test
    lines.append(line)

    y = 230
    for l in lines[:3]:
        _, _, w, _ = draw.textbbox((0, 0), l, font=font_small)
        draw.text(((width - w) / 2, y), l, fill="white", font=font_small)
        y += 40

    draw.text((30, height - 50), "QuickBlog", fill="white", font=font_small)

    filename = f"seed_{category_name.lower()}_{index}.png"
    filepath = os.path.join(UPLOAD_DIR, filename)
    img.save(filepath, "PNG")
    return filename


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def seed_blogs():
    app = create_app()
    with app.app_context():
        user = User.query.filter_by(role="admin").first()
        if not user:
            print("No admin user found. Run setup.py first.")
            return

        existing = Blog.query.count()
        if existing > 8:
            print(f"[•] {existing} blogs already exist. Skipping seed (delete blogs first if you want to re-seed).")
            return

        created = 0
        for category_name, blogs in BLOG_DATA.items():
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                print(f"[!] Category '{category_name}' not found. Run setup.py first.")
                continue

            for i, blog_info in enumerate(blogs):
                days_ago = random.randint(1, 60)
                created_at = datetime.utcnow() - timedelta(days=days_ago)

                thumbnail = generate_placeholder_image(category_name, blog_info["title"], i)

                blog = Blog(
                    title=blog_info["title"],
                    subtitle=blog_info["subtitle"],
                    description=blog_info["description"],
                    thumbnail=thumbnail,
                    status="published",
                    featured=(i == 0),
                    views=random.randint(50, 3000),
                    category_id=category.id,
                    user_id=user.id,
                    created_at=created_at,
                )
                db.session.add(blog)
                created += 1
                print(f"  ✓ [{category_name}] {blog_info['title'][:60]}...")

        db.session.commit()
        print(f"\n✅ {created} blogs created with generated images in static/uploads/")


if __name__ == "__main__":
    print("Seeding blogs for all categories...\n")
    seed_blogs()
