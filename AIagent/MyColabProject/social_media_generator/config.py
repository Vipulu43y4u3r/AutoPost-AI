# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # OpenAI Configuration
    GPT_CONFIG = {
        "config_list": [{"model": "gpt-4-turbo-preview", "api_key": OPENAI_API_KEY}],
        "timeout": 120,
        "temperature": 0.7,
    }

    GPT_VISION_CONFIG = {
        "config_list": [{"model": "gpt-4o", "api_key": OPENAI_API_KEY}],
        "timeout": 120,
        "temperature": 0.7,
    }

    DALLE_CONFIG = {
        "config_list": [{"model": "dall-e-3", "api_key": OPENAI_API_KEY}],
        "timeout": 120,
        "temperature": 0.7,
    }

    # Application Settings
    CACHE_DIR = ".cache/"
    OUTPUTS_DIR = "outputs/"
    IMAGES_DIR = "outputs/images/"
    POSTS_DIR = "outputs/posts/"
    
    # Streamlit Settings
    PAGE_TITLE = "AI Social Media Post Generator"
    PAGE_ICON = "📱"
    LAYOUT = "wide"

# backend/utils/constants.py
# Platform specifications for different social media platforms
PLATFORM_SPECS = {
    "instagram": {
        "image_sizes": {
            "square": (1080, 1080),
            "portrait": (1080, 1350),
            "story": (1080, 1920)
        },
        "caption_length": 2200,
        "hashtag_limit": 30,
        "optimal_hashtags": "8-15"
    },
    "linkedin": {
        "image_sizes": {
            "horizontal": (1200, 627),
            "square": (1080, 1080)
        },
        "caption_length": 3000,
        "hashtag_limit": 5,
        "optimal_hashtags": "3-5"
    },
    "twitter": {
        "image_sizes": {
            "horizontal": (1024, 512),
            "square": (1080, 1080)
        },
        "caption_length": 280,
        "hashtag_limit": 2,
        "optimal_hashtags": "1-2"
    },
    "facebook": {
        "image_sizes": {
            "horizontal": (1200, 630),
            "square": (1080, 1080)
        },
        "caption_length": 63206,
        "hashtag_limit": 30,
        "optimal_hashtags": "1-3"
    }
}

POST_TYPES = [
    "Educational",
    "Motivational",
    "Behind-the-scenes",
    "Product/Service Promotion",
    "User-generated Content",
    "News/Updates",
    "Entertainment",
    "Question/Poll",
    "How-to/Tutorial",
    "Inspirational Quote"
]

TONES = [
    "Professional",
    "Casual",
    "Humorous",
    "Inspirational",
    "Urgent",
    "Friendly",
    "Authoritative",
    "Playful",
    "Empathetic",
    "Confident"
]

VISUAL_STYLES = [
    "Modern/Minimalist",
    "Colorful/Vibrant",
    "Professional/Corporate",
    "Artistic/Creative",
    "Vintage/Retro",
    "Tech/Futuristic",
    "Natural/Organic",
    "Bold/Striking",
    "Elegant/Sophisticated",
    "Fun/Playful"
]