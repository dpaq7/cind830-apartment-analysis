#!/bin/bash
# Script to push to GitHub
# Replace YOUR_USERNAME with your actual GitHub username

echo "🚀 Pushing CIND830 Apartment Analysis to GitHub..."
echo "📝 Make sure you've created the repository on GitHub first!"
echo ""

# Replace YOUR_USERNAME in the line below
read -p "Enter your GitHub username: " USERNAME

echo "Adding GitHub remote..."
git remote add origin https://github.com/$USERNAME/cind830-apartment-analysis.git

echo "Setting main branch..."
git branch -M main

echo "Pushing to GitHub..."
git push -u origin main

echo "✅ Done! Your repository should now be available at:"
echo "🔗 https://github.com/$USERNAME/cind830-apartment-analysis"